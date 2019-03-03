import sys
import openpyxl
 
def xlsx_to_txt(input_file, output_file, column):
    output_file = open(output_file, "w+") #output file where data are save
    input_file = input_file.__str__() #input xlsx file where is data
    column = column.__str__() #input clumn example A B C D E F G H etc.
    book = openpyxl.load_workbook(input_file) #open xsxl file and loat to workbook
    sheet = book.active #load spreadsheet as active
    first_column = sheet[column] #load whole column of index 'column'
    i=1
    while i < len(first_column):
        # load i-column from spreadsheet and save it to i-line in output file
        output_file.write(first_column[i].value.__str__() + '\n')
        #print(first_column[i].value.__str__())
        i+=1
    output_file.close() #close output file
 
if __name__ == "__main__":
    input_file = sys.argv[1] #Input file name
    output_file = sys.argv[2] #Output file name
    column = sys.argv[3] #Column
    xlsx_to_txt(input_file,output_file,column)
