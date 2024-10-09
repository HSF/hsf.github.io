## Final Project Report
![image](https://github.com/user-attachments/assets/61e8cdd3-09e9-4207-97e6-167bd31c78c3)

- **Organization**: CERN HSF
- **Mentors**: Gianmaria Del Monte, Enrico Bocchi , Roberto Valverde, Zachary Goggin
- **Project Size**: Large (350 h)
- Name: Yash Raj Singh
- Email: yashraj14700728@gmail.com
- Github: [yrs147](https://github.com/yrs147)
- **Gitlab Branch(My Work)** : https://gitlab.cern.ch/cback/restic-backup-agent/-/tree/containerise

## Project Abstract

The Storage department at CERN is responsible for the preservation and backup strategy of 880PB+ of disk based data across various storage infrastructure solutions. Excluding physics data, Backups must also be provided for internal user facing name-spaces, one of the main projects used for this purpose at Cern is CBACK (Cern Backup.)

The Storage department at CERN faces the challenge of preserving and backing up vast amounts of disk-based data across diverse storage infrastructure solutions. In addition to physics data, internal user-facing namespaces require backups, for which CBACK (CERN Backup) is a primary solution. CBACK is an adaptable backup orchestrator utilizing Restic alongside a central SQL database to manage various job types such as Backup, Restore, Prune, and Verify. These jobs are executed by stateless agents, and the current infrastructure, deployed on VMs, lacks scalability due to manual expansion processes.

This project aimed to enhance the flexibility and scalability of CBACK by introducing dynamic agent spawning through Kubernetes-based scheduling. The project was responsible for developing a new "scheduler" agent type responsible for monitoring the internal database and initiating agent creation based on service demand. Additionally, the project also had containerisation as one of its primary goals to enable dynamic spawning of  agents by the scheduler in a kubernetes environment. And to limit the scope of changes CSI drivers were also integrated along with cephx keys allowing for the restriction of file mount scopes  on containers running job agents. 

By breaking the static nature of infrastructure deployment and enabling automated scaling, this project aimed to significantly enhance the efficiency and adaptability of CERN's backup orchestration system, ensuring reliable preservation and backup strategies for critical data.

## Deliverables

1. **Containerisation and Helm Chart Adaptations**: Modify existing agents within CBACK to enable containerisation and spawning by the new scheduler agent. This involves updating Helm charts and making necessary code changes to ensure seamless integration with Kubernetes-based deployment environments..

  
2. **Development of Scheduler Agent**: Implement a new "scheduler" agent type responsible for monitoring the internal database of CBACK. The scheduler will be designed to analyze service demand and dynamically spawn other agents as required. This functionality will be crucial for achieving scalability and flexibility within the CBACK infrastructure.


3. **Scope Limitation for File Mounts**: Collaborate with the team to implement changes that allow for the limitation of scope within the file mounts of a node or container running a job agent. This will involve utilising cephx keys to enforce restrictions and enhance security and control over data access within the CBACK ecosystem.


## Technologies used 

- Python
- Kubernetes
- Helm
- CSI Drivers
- MySQL
- Ceph

## Work Done


Prior to the implementation of the Scheduler Agent in the CBACK project, the backup orchestration process involved significant manual overhead. Operators had to manually monitor and trigger various backup, restore, and pruning jobs using the `cback` command line utility. This static infrastructure relied on virtual machines (VMs) where agents for each job type were manually configured and managed.
![image](https://github.com/user-attachments/assets/212b37bc-5603-4136-ae02-611bf17b959f)



As the demand for backup operations fluctuated, the operators faced challenges in scaling the number of agents efficiently. Each job type—backup, restore, prune, verify—required a dedicated agent running on a static VM, leading to potential bottlenecks and delays in processing. This rigid setup made it difficult to adapt to changing workloads, resulting in inefficiencies and a higher likelihood of human error.


Now I divided the whole project into 3 phases :-
- Containerisation
- Implementing Scheduler Agent
- Integration CSI Drivers and Cephx Keys

### Phase 1: Containerisation

The initial phase involved containerising`cback` for it to be able to run in a kubernetes cluster.
I began by creating a docker image for this repository by adding in commands which were required to setup the project . Once that was done the image was for in a harbor image registry .

the next part was building the helm charts to simplify deployment of cback on a k8s cluster 
Helm chart which was finalized in the end looked like this 

```
cback-helm-chart/
├── Chart.yaml
├── templates
│   ├── cback-pod.yaml
│   ├── cback-rolebinding.yaml
│   ├── cback-role.yaml
│   ├── cback-serviceaccount.yaml
│   ├── cback-service.yaml
│   ├── csi-cephx-secret.yaml
│   ├── _helpers.tpl
│   ├── mysql-pod.yaml
│   ├── mysql-secret.yaml
│   ├── mysql-service.yaml
│   └── storageclass.yaml
└── values.yaml
```

### Phase 2: Implementing the Scheduler

With the introduction of the Scheduler Agent, the CBACK project now operates with a dynamic job management system that significantly reduces manual intervention and improves scalability. The Scheduler Agent acts as an intermediary between user requests and the Kubernetes cluster, allowing jobs to be executed in response to real-time service demand.

#### Scheduler Agent Workflow

![image](https://github.com/user-attachments/assets/9701dbee-de17-416e-8411-1b76c1eac931)




1. A user creates a job using the `cback` command line utility and enables it for processing.

2. The job request is picked up by the Scheduler Agent, which interacts with a dedicated scheduler repository. This repository is responsible for querying the MySQL database where various procedures are installed.

3. The MySQL procedures emit the job ID to the Scheduler Agent, indicating that a job is ready for execution.

4. The Scheduler Agent then spawns the corresponding job agent (e.g., backup agent, restore agent) through a Kubernetes job.

5. These Kubernetes jobs are attached to Persistent Volume Claims (PVCs), which claim a Persistent Volume (PV) that mounts the job's source directory to the root of the corresponding CephFS cluster filesystem.

6. The spawned agent runs the job in the Kubernetes cluster.


### Phase 3: Integration of CSI Drivers and Cephx Keys

In this phase, the goal was to ensure that the job pods could only access the required directories in the Ceph cluster, where the backup jobs would perform their actions. To achieve this, we integrated Ceph CSI drivers, which are crucial for managing storage volumes in Kubernetes environments and used Cephx Keys limit the scope of mount.



We explored two approaches for mounting the necessary storage:

1. **Dynamic Provisioning**:

![image](https://github.com/user-attachments/assets/f6893c16-b42d-4a4d-8026-2738883b7cc5)



- This approach allows Kubernetes to automatically create Persistent Volumes when a Persistent Volume Claim  is made.
- A storage class was defined in the Kubernetes cluster to facilitate this dynamic provisioning.
- When the Scheduler Agent creates a job, it would also create a corresponding PVC, which would request a volume from the storage class and automatically mount it to the job pod.

 While testing dynamic provisioning, we faced a significant limitation regarding subvolume groups. For instance, if we intended to mount a pod to the root of the Ceph cluster e.g `/cephfs-miniflax`, the provisioner would only allow for the creation of a subvolume tied into a subvolumegroup instead. Therefore, if a job was set to operate on a specific path like `/cephfs-miniflax/volumes/_nogroup/miniflax_snaps/zgoggins` the pod would actually attempt to mount to a root path like `/cephfs-miniflax/<subvolume-group-name>/<dynamic-id-forsubvolume>` and it wasn't possible to overide to mount to an arbitrary path. This meant the scheduler could not locate the specified source path, leading to complications in job execution.
 
2. **Static Provisioning**:

![image](https://github.com/user-attachments/assets/331bb1c9-e012-4e20-a207-fa17ae87e7a5)



- This approach involves defining PV and PVC pairs manually in the Helm charts.

- By specifying PV and PVC pairs for each job in the Helm charts, we could ensure that each job would mount to the correct path in the Ceph cluster without any unexpected subdirectories.

- **Implementation**: In our Helm charts, we defined the required PVs and PVCs, ensuring that each job pod would mount to its corresponding PVC according to the cluster it was running on. This way, the paths were predictable, and job execution could proceed without the issues presented by dynamic provisioning.


Static provisioning also have a few negatives, in this approach it becomes difficult to isolate a job with a specific cephx key e.g. the PV / PVC's are shared between the pods, for a give mount path / cluster. This can partially be elevated by having read only and write only PV's to limit scope, however further granularity is harder to achieve with non dynamic PV / PVC's.

Static Provisioning also requires some overhead from the user installing the helm chart, as they must define their PV / PVC templates prior to installing, this is also partially the case with dynamic provisioning (and storage classes) but is much simpler to do in the latter case.

## Conclusion

By transitioning to a Kubernetes-based infrastructure with dynamic agent spawning, integrating Ceph CSI drivers, and employing static provisioning for storage, we have significantly enhanced the usability, scalability, and reliability of the cern backup system.

## Future scope

The CBACK project has laid a solid foundation for scalable and efficient backup orchestration at CERN, but there are several avenues for further enhancement:

1. **Custom Provisioner Development**: To address the limitations encountered with subvolume groups in dynamic provisioning, a custom provisioner can be implemented. This provisioner would allow for arbitrary root paths that are not constrained by volume groups, ensuring that the specific source paths are correctly aligned with job requirements.
    
2. **Automation of Cephx Key Management**: Currently, the process of fetching Cephx keys from the CBACK portal in Manila involves using a set of testing key pairs. Future developments should focus on automating this key retrieval process . 

3. **Integration of CSI Drivers for EOS**: Future work can focus on integrating Container Storage Interface drivers for EOS, to expand the capabilities of the backup system.
