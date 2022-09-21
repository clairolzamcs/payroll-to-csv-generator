import csv
import json
from datetime import datetime
import calendar

# declare globals
unique_eids,all_items,computed_values = [],[],[]
pay_group = {
    'A': 20,
    'B': 30
}

def scrape_data(csv_file_path):
    with open(csv_file_path,'r', encoding="utf-8-sig", errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        del all_items[:]
        for row in reader:
            # declare variables
            start_date = datetime.today().strftime('%d/%m/%Y')
            end_date = datetime.today().strftime('%d/%m/%Y')
            
            # get values
            date_string = row['date']
            eid = row['employee id']
            hours_worked = row['hours worked']
            work_day = datetime.strptime(date_string, '%d/%m/%Y')
            
            # store unique eid
            if eid not in unique_eids:
                unique_eids.extend(eid)
            
            # compute amount_paid based on hours and pay group
            amount_paid = float(hours_worked) * float(pay_group.get(row['job group']))                                                           
            
            # push data to a new local array
            item_complete_details = [eid,amount_paid]
            
            # compute for the correct start and end dates and cutoff then push data to local array
            item_complete_details.extend(get_cutoff_start_end_dates(work_day))
            
            # push local array to the global array            
            all_items.append(item_complete_details)
        
def compute_total_per_cutoff(unique_eids,all_items):
    del computed_values[:]    
    # read all_items and compute total amount per cutoff per employee
    for eid in unique_eids:
        cutoff_1_amount,cutoff_2_amount = 0,0
        item_computed_1,item_computed_2 = [],[]
        del item_computed_1[:]
        del item_computed_2[:]

        for item in all_items:      
            # check if item eid is equal to currently selected eid
            if str(item[0]) == str(eid):                      
                if 'cutoff_1' in item:
                    cutoff_1_amount =  cutoff_1_amount + item[1]
                    start_date = item[2]
                    end_date = item[3]
                    # push data to a local array
                    item_computed_1 = [eid,start_date,end_date,cutoff_1_amount]
                else:
                    cutoff_2_amount =  cutoff_2_amount + item[1]
                    start_date = item[2]
                    end_date = item[3]
                    # push data to a local array
                    item_computed_2 = [eid,start_date,end_date,cutoff_2_amount]
        
        # after scanning all items and tallying all under the selected eid, push to the global array computed_values        
        if item_computed_1: computed_values.append(item_computed_1) 
        if item_computed_2: computed_values.append(item_computed_2)

def get_cutoff_start_end_dates(work_day):
    cutoff = ''
    if ( work_day.day > 15 ):
        # falls in cut_off_2
        start_date = work_day.replace(day=16)
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = work_day.replace(day=calendar.monthrange(work_day.year, work_day.month)[1])
        end_date = end_date.strftime('%Y-%m-%d')
        cutoff = "cutoff_2"
    else:
        # falls in cut_off_1
        start_date = work_day.replace(day=1)
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = work_day.replace(day=15)
        end_date = end_date.strftime('%Y-%m-%d')
        cutoff = "cutoff_1"
    
    data = [start_date,end_date,cutoff]
    return data
            
def generate_dict(computed_values):
    # generate json using the array that contains accumulated computed data
    employeeReports,payrollReport_dict = [],{}    

    del employeeReports[:]
    for item in computed_values:
        payPeriod = {}
        payPeriod['startDate'] = item[1]
        payPeriod['endDate'] = item[2]
        
        employeeReports_dict = {}
        # Delete all elements from the dictionary

        employeeReports_dict.clear()            
        employeeReports_dict['employeeID']=int(item[0])
        employeeReports_dict['payPeriod']=payPeriod
        employeeReports_dict['amountPaid']=item[3]
        
        employeeReports.append(employeeReports_dict)
    
    payrollReport_dict.clear()
    payrollReport_dict = {
        "payrollReport": {
            "employeeReports": employeeReports
        }
    }
    
    return (payrollReport_dict)

def run_steps(csv_file_path):
    scrape_data(csv_file_path)
    compute_total_per_cutoff(unique_eids,all_items)
    return generate_dict(computed_values)
   
# csv_file_path = 'time-report-42.csv'
if __name__ == '__main__':
    run_steps(csv_file_path)