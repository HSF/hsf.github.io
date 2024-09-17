# Lossless compression of raw data for the ATLAS experiment at CERN

### Abstract
The goal of this project is to study the performance and effectiveness of various compression algorithms, specifically on ATLAS RAW data. The ATLAS experiment produces extremely large amounts of data, and it is only expected to increase with future planned upgrades within the LHC. Prior studies into compression of the data has shown that due to the highly redundant nature of the generated data, lossless data compression algorithms are extremely effective in reducing the binary size of ATLAS data. Here, we would like to find an algorithm that has a good balance of compression time, and compressed binary size.

### Process

This project can be split into two major parts. The first was studying which compression library should be used, mainly by looking at how effective different libraries are at compressing ATLAS RAW data. The second was modernizing the aforementioned [ATLCopyBSEvent.cxx](https://gitlab.cern.ch/atlas/athena/-/blob/main/Event/ByteStreamCnvSvc/test/AtlCopyBSEvent.cxx), as well as integrating the chosen compression library for the files being processed.

To assist with the former, I made use of [lzbench](https://github.com/inikep/lzbench), a tool created to benchmark a variety of different LZ77/LZSS/LZMA compression libraries, with the command ``` lzbench -ebrotli/zstd/lzlib/xz/zlib/lz4 decompressed.data``` where decompressed.data is an example ATLAS raw data file (in this case, the data displayed below is gathered from /cvmfs/atlas-nightlies.cern.ch/repo/data/data-art/Tier0ChainTests/TCT_Run3/data22_13p6TeV.00431493.physics_Main.daq.RAW._lb0525._SFO-16._0001.data, although I also tested with varying files to very similar results). All of the libraries and forms of compression use very similar methods to compress and decompress data, although each library will have varying quirks and capabilities that may be better or worse for our purposes here. 

Below is a table of data for compressors that were thought to be relevant to look at. One thing that is important to note is that much of the ATLAS experiment data has previously used zlib with compression level 1 for compression, so it will be treated as something of a baseline and the remaining libraries will be compared to it. Below are tables of libraries that were thought to be particularly notable, for each, we take note of the library used and what compression level, the ratio ((compressed size / original size) * 100), as well as compression and decompression speed.

| Library | Level | Ratio | Compression | Decompression |
|---------|-------|-------|-------------|---------------|
|zlib | 1 | 62.23 | 67.7 MB/s |  234 MB/s |
|zlib | 2 | 61.84 | 60.2 MB/s |  223 MB/s |
|zlib | 3 | 61.33 | 49.6 MB/s |  222 MB/s |
|zlib | 4 | 60.99 | 47.0 MB/s  | 240 MB/s |
|zlib | 5 | 60.39 | 32.9 MB/s |  219 MB/s |
|zlib | 6 | 60.02 | 22.5 MB/s  | 226 MB/s |
|zlib | 7 | 59.88 | 18.4 MB/s  | 218 MB/s |
|zlib | 8 | 59.76 | 12.0 MB/s  | 218 MB/s |
|zlib | 9 | 59.71 | 6.96 MB/s |  219 MB/s |

| Library | Level | Ratio | Compression | Decompression |
|---------|-------|-------|-------------|---------------|
|zstd | 1 | 62.61 | 457 MB/s  | 670 MB/s |
|zstd | 2 | 61.68 | 365 MB/s | 896 MB/s |
|zstd | 3 | 60.68 | 265 MB/s  | 903 MB/s |
|zstd | 4 | 60.12 | 156 MB/s  | 474 MB/s |
|zstd | 5 | 59.48 | 106 MB/s |  494 MB/s |
|zstd | 6 | 58.99 | 83.6 MB/s |  511 MB/s |
|zstd | 7 | 58.45 | 74.4 MB/s | 1037 MB/s |
|zstd | 8 | 58.35 | 65.6 MB/s |  525 MB/s |
|zstd | 9 | 57.94 | 54.3 MB/s |  976 MB/s |
|zstd | 10 | 57.60 | 41.3 MB/s |  424 MB/s |
|zstd | 11 | 57.52 | 27.7 MB/s |  805 MB/s |
|zstd | 12 | 57.48 | 23.8 MB/s |  487 MB/s |
|zstd | 13 | 57.54 | 11.6 MB/s |  493 MB/s |
|zstd | 14 | 57.49 | 10.6 MB/s  | 946 MB/s |
|zstd | 15 | 57.39 | 8.65 MB/s | 1093 MB/s |
|zstd | 16 | 55.79 | 7.32 MB/s |  907 MB/s |
|zstd | 17 | 55.56 | 4.62 MB/s | 909 MB/s |
|zstd | 18 | 55.10 | 3.84 MB/s  | 469 MB/s |
|zstd | 19 | 54.83 | 2.91 MB/s  | 490 MB/s |

| Library | Level | Ratio | Compression | Decompression |
|---------|-------|-------|-------------|---------------|
|brotli | 0 | 64.80 | 354 MB/s  | 221 MB/s |
|brotli | 1 | 62.79 | 233 MB/s  | 225 MB/s |
|brotli | 2 | 59.91 | 163 MB/s  | 259 MB/s |
|brotli | 3 | 59.66 | 119 MB/s  | 252 MB/s |
|brotli | 4 | 57.74 | 57.1 MB/s |  268 MB/s| 
|brotli | 5 | 56.65 | 31.4 MB/s |  252 MB/s|
|brotli | 6 | 56.31 | 21.9 MB/s  | 218 MB/s|
|brotli| 7 | 56.09 | 13.2 MB/s  | 234 MB/s|
|brotli | 8 | 55.95 | 8.81 MB/s  | 245 MB/s|
|brotli  | 9 | 55.78 | 6.57 MB/s  | 241 MB/s|
|brotli | 10 | 49.90 | 1.00 MB/s |  161 MB/s|
|brotli | 11 | 50.31 | 0.55 MB/s  | 147 MB/s|

| Library | Level | Ratio | Compression | Decompression |
|---------|-------|-------|-------------|---------------|
|lzlib | 0 | 54.82 | 22.3 MB/s | 32.5 MB/s |
|lzlib | 1 | 53.49 | 10.0 MB/s  | 34.5 MB/s |
|lzlib | 2 | 52.75 | 7.64 MB/s | 33.4 MB/s |
|lzlib | 3 | 51.74 | 5.50 MB/s | 33.4 MB/s |
|lzlib | 4 | 51.28 | 4.30 MB/s | 35.1 MB/s |
|lzlib | 5 | 50.84 | 3.37 MB/s | 35.2 MB/s |
|lzlib | 6 | 50.30 | 2.30 MB/s | 33.7 MB/s |

| Library | Level | Ratio | Compression | Decompression |
|---------|-------|-------|-------------|---------------|
|xz | 0 | 54.67 | 17.8 MB/s | 38.5 MB/s |
|xz | 1 | 53.89 | 15.8 MB/s | 40.5 MB/s |
|xz | 2 | 53.56 | 9.04 MB/s | 39.9 MB/s |
|xz | 3 | 53.44 | 5.78 MB/s | 42.8 MB/s |
|xz | 4 | 50.94 | 3.82 MB/s | 41.3 MB/s |
|xz | 5 | 50.31 | 2.77 MB/s | 42.1 MB/s |
|xz | 6 | 50.27 | 2.87 MB/s | 40.2 MB/s |

While the above is largely a dump of data collected, we will do some analysis to come to a conclusion about which compression library we think will be most effective for our purposes. To start, one notable upside is that almost all of the libraries, by virtue of being different forms of dictionary compression at their core, have decompression speeds that are fairly agnostic of the compression level and ratio. This, along with the fact that we care more about compression ratio for overall space-saving effectiveness and compression speed for realtime time-saving effectiveness, decompression speed will play a very small, if any, role in the decisions made after this. We can also see clearly that as we increase the compression levels for every library, they plateau very quickly. In general, the lowest and highest compression levels within a single library may only see a few percent difference in compression level, while being over an order of magnitude slower.

Below we are plotting compression speed and compression ratio generated by the above data plotting in this [colab](https://colab.research.google.com/drive/12uCIDyMJEIvKDe3O2V4KeugHHjqZYKlV?usp=sharing):

![ratio vs speed](https://github.com/user-attachments/assets/68119bd4-daa7-406e-9787-fc1ab7d3110a)

The ideal library would have high compression speed and low compression ratio. We can see that brotli covers the widest range, giving us the option to have the slowest compression speed in exchange for the lowest compression ratio, but also the second-fastest speed with the highest ratio. It is also immediately noticeable that zlib consistently gives compression ratios that are higher than desirable for the speed being compressed. Both xz and lzlib perform very similarly, where they do not offer the same range of options that brotli and zstd do, and they only operate in the slower and lower compression ratio end of the spectrum, but they are an improvement over brotli and zstd within that range. 

In the end, to compare each library with the most similar compression speed to zlib at compression level 1 we see:
| Library | Level | Ratio | Compression | Decompression |
|---------|-------|-------|-------------|---------------|
|zlib | 1 | 62.23 | 67.7 MB/s |  234 MB/s |
|zstd | 8 | 58.35 | 65.6 MB/s |  525 MB/s |
|brotli | 4 | 57.74 | 57.1 MB/s |  268 MB/s| 

Whereas when looking at the most similar compression ratios  we see:
| Library | Level | Ratio | Compression | Decompression |
|---------|-------|-------|-------------|---------------|
|zlib | 1 | 62.23 | 67.7 MB/s |  234 MB/s |
|zstd | 1 | 62.61 | 457 MB/s  | 670 MB/s |
|brotli | 1 | 62.79 | 233 MB/s  | 225 MB/s |

*lzlib and xz are not exactly comparable, their compression is much slower but with much lower ratios across their entire operable range.

Here we see that if we are looking to get a similar compression ratio, zlib performs the slowest by far at close to a fourth of the speed brotli, and zstd reaches almost two times brotli's speed. If we are looking to get similar compression times, while we do not have as close of a match as compression ratio, both zstd and brotli result in a reduction of a few percent of the original filesize.  

Given the data collected, we chose to use zstd as our compression algorithm. This decision came for many reasons and was primarily determined by the analysis above. The goal for this project was to find a faster replacement for the currently in-place Zlib compression system, with particular importance on compression ratio rather than compression speed. The reason for this is that when we look at the scale of data generated by the ATLAS experiment, a reduction of even a few percentages makes a large difference when the filesizes are upwards of exabytes. The two most relevant graphs for this comparison are the two smaller ones looking at zlib, zstd, and brotli at fixed metrics. For example, we see that if we wanted to keep the compression ratio of the system the same, switching from zlib to zstd would still yield improvements of roughly 7 times in compression speed, and 3 times in decompression speed. However, because we are looking to keep the compute resources required roughly the same, we instead hold the compression speed as close to fixed as possible. This gives us the first of the two smaller tables above where we see that, in terms of compression speed, zlib at level 1, zstd at level 8, and brotli at level 4 are very roughly equal. We now see slight differences in the compression ratio, where brotli offers the best compression, followed closely by zstd, and zlib trails behind by a slightly more notable portion. 

Given the above comparisons, a natural question may be, why ztd? Brotli at first glance compresses more efficiently than zstd, and since it is the best metric why not choose that? There were a variety of factors that went into this decision: for one, zstd performs as a very good all-rounder. It compresses slightly faster than brotli and decompresses much faster, sacrificing only 0.5% of the original filesize in compression ratio for this win. Additionally, it offers a fairly wide range of potential settings in the advanced API, including using dictionaries to train better compression and streaming compression for files where we gain the input in fragments at a time. This opens up the possibility of future exploration that I was not able to look at this summer. Finally, zstd is guaranteed to be stable. The format used by zstd is very stable and well documented, the project is fully open source, it is guaranteed to be supported in the future and sees frequent maintenance/updates, and it is already pre-bundled in many popular Linux distributions. The last point was particularly important for CERN, where these files are expected to be compressed and kept for long periods of time till they are decompressed and used at some point in the future, so stability is a must.

The next step was to go through ATLCopyBSEvent.cpp and modernize it, then integrate zstd. I started this process by stripping back the file such that it could only perform the basic operations that it needed: reading, writing, and copying files. Much of the code was removed with the capability to read and write from collections because it was deemed non-essential. Then, starting with this bare-bones version, I ran the program on some existing files that were pre-compressed to various levels, ensuring that it would still be possible to read the files in their varying states and write them out. Once this was ensured, I moved on to modernizing the code. In its old state, there was lots of room for misuse of objects with lots of raw C pointers being passed around, as well as lots of cases of small errors such as passing the raw pointer obtained from std::unique_ptr<T>.get() to a function, rather than moving it. Fixing these issues made the code appear much cleaner, and also meant that we got rid of any potential memory-related issues that could've arisen if the system were used in a larger context. I also added clang-format, to automatically format the code for consistency with the rest of the Atlas codebase.

The final step was then to integrate zstd into the system. I had previously moved the logic to write out data into a C++ lambda such that it could more easily be reused. At this step, we have a fragment of data retrieved from our dataReader, I used the simple zstd compression API to take this pre-allocated fragment of data, and then write it out as pre-compressed data with our dataWriter. It is important to use the function putPrecompressedData() rather than putData(), because looking at the internal implementations of the two, we can see that they are wrappers around the same internal function with different settings for whether or not we want to compress the data using zlib. Using putData would result in a file that has been compressed twice which would not be useable in our system. This method of compression is also convenient because it means that individual events remain separate, with all of their metadata being written out as usual. With the decompression step being inserted as the aforementioned fragments are read in by the dataReader, we can decompress each event without having to worry about decompressing and recompressing the full file.

### Conclusion
All in all, I had a great Summer working with CERN to investigate data compression methods for the ATLAS experiment. It was a very good learning experience, although daunting at times, having the opportunity to work in a large existing codebase on a project with real-world impact. I hope that my research over the Summer will prove useful for future compression-related endeavors at CERN. I would like to extend thanks to my mentor, Maciej Szymanski for this opportunity, as well as all of his very much needed help over the Summer. I definitely could not have completed the project without his guidance and valuable mentorship.

The final code for the project is available [here](https://github.com/Ish-D/AtlEventProcess)
