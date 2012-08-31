import re

date_pattern = re.compile(r'^(\d{1,2})[\.\-](\d{1,2})$',re.M)

def parse_date(data):
    dates = re.search(date_pattern,data)
    if dates:
        return [fill_zero(d) for d in dates.groups()]

def test_date():
    assert parse_date('3.14') == ['03','14']
    assert parse_date('3.4') == ['03','04']
    assert parse_date('') == None

record_pattern = re.compile(r'^([\d:-]+)\t+([\w,]+)\t+(.+)$',re.M)

def parse_record(data):
    result = re.search(record_pattern,data)
    if result:
        return result.groups()

def test_record():
    s = '11:00-11:50	git		pro git'
    assert parse_record(s) == ('11:00-11:50', 'git', 'pro git')
    assert parse_record('') == None

def test():
    test_date()
    test_record()


def fetch_record(filename):
    def parse_time(atime):
        #'8:30' -> '08:30'
        return ':'.join([fill_zero(t) for t in atime.split(':')])

    f = open(filename,'r')
    currentYear = '2012'
    currentDate = ''
    for line in f:
        dates = parse_date(line)
        if dates:
            currentDate = '%s-%s-%s' %(currentYear,dates[0],dates[1])
            continue
        else:
            records = parse_record(line)
            if records:
                time_str,tag_str,content = records

                start_time,end_time = time_str.split('-')
                start_time = parse_time(start_time)
                end_time = parse_time(end_time)

                start_datetime = '%s %s:00' %(currentDate,start_time)
                end_datetime = '%s %s:00' %(currentDate,end_time)

                tags = tag_str.split(',')

                yield start_datetime,end_datetime,tags,content

    f.close()

def fill_zero(data):
    if len(data) == 1:
        data = '0'+data
    return data

def show_time(seconds):
    minutes = seconds/60
    hours = minutes//60
    return '%4dh\t%4dm' %(hours,minutes - hours * 60)

from datetime import datetime
def statistics(filename):
    result = {}
    for start_datetime,end_datetime,tags,content in fetch_record(filename):
        #print start_datetime,end_datetime,tags,content.decode('utf8')
        s_time = datetime.strptime(start_datetime,"%Y-%m-%d %H:%M:%S")
        e_time = datetime.strptime(end_datetime,"%Y-%m-%d %H:%M:%S")
        seconds = (e_time - s_time).total_seconds()

        for tag in tags:
            atime = seconds/len(tags)
            result.update({tag:result.get(tag,0) + atime})

    for tag,seconds in result.iteritems():
        print '%s\t%s' %(tag,show_time(seconds))

def arrange(filename):
    result = {}
    for start_datetime,end_datetime,tags,content in fetch_record(filename):
        for tag in tags:
            #content = content.decode('utf8')+'\n'
            content = content+'\n'
            result.update({tag:result.get(tag,'') + content})

    for tag,content in result.iteritems():
        print '===================='
        print tag
        print '-----'
        print content

if __name__ == '__main__':
    #test()
    filename=r'diary/2012-8.rst'
    statistics(filename)
    arrange(filename)
