# 2020. 5. 12.
# result file로부터 데이터 불러오기
# Read One data frame from SOF_output file

##############################################################
# Function Declaration
def SOFReaderInitializer(filename):
    print("[START]\t SOFReaderInit \n")

    ret = open(filename, "r")

    print("[END]\t SOFReaderInit \n")
    return ret

def SOFCallOneFrameInfoFromfile(fp, frame_count, sof_size, dgps_size):
    print("[START]\t SOFReaderMain \n")

    

    print("[END]\t SOFReaderMain \n")


##############################################################
# 1. Open data file from folder
print("[START]\t SOF result reader example \n")

read_filename = 'testfile.txt'
#filename2 = '0507_1247_ALL_input_SOF_Result.bin'
ret = SOFReaderInitializer(read_filename)


# 2. Read One frame (w/ frame number) 


# 3. Close data file


print("[END]\t SOF result reader example \n")




    


