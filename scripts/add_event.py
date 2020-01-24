import yaml


def ask_yn():
    pass

# checkers
def is_date()

def is_date_after(before: Union[str, ..], after: Union[str, ...])
    # checks both dates

def is_date_before(after, before):
    return is_date_after(before, after)

def is_unique_url(url, urls)

def not_blank(inpt):
    bool(inpt)

def join_checkers(checkers):
    def checker(inpt):
        check = True
        message = ""
        for checker in checkers:
            res = checker(inpt)
            check &= res.check
            message += res.message
    return checker

def input_field(prompt, checker=None):
    accepted = False
    while not accepted:
        ans = input(prompt)
        if checker is None:
            return ans
        check = checker(ans)
        if not check.pass:
            print(check.message)
            override = ask_yn("Override warning and still accept?")
            if override:
                return ans
            else:
                continue
        else:
            return ans


def check_event(event):
    pass


class EventDatabase(object):
    def __init__(self, events):
        self.events = events
    
    @class_method
    def from_file(path):
        with open("example.yaml") as stream:
            events = yaml.safe_load(stream)
        return EventDatase(events)
    
    def write(path):
        with open("example.yaml", "w") as stream:
            stream.dump(self.events, stream)
        
    def add_event(event):
        self.events.append(event)



name = input_field("Event name", not_blank)
start_date = input_field("Start date [YYYY-MM-DD]", is_date)
end_date = input_field("End date [YYYY-MM-DD]", lambda inpt: is_date_after(inpt, start_date))
deadline = input_field("Deadline [YYYY-MM-DD]", lambda inpt: is_date_before(inpt, start_date))
url = input_field("Url", lambda url: is_unique_url(inpt, 
