class FBStock:
    def __init__(self):
        self._fileObj=None
        self._stockobjects=[]
    def openFile(self):
        while not self._fileObj:
            filename=raw_input("Enter Filename:")
            try:
                self._fileObj=file(filename)
            except IOError:
                Print "Enter valid filename"
    def get_data_list():
        line=self._fileObj.readline()
        while line:
            linelist=split.line
            self.addAccount(linelist[1],linelist[0],float(linelist(2)))
            line=self._fileObj.readline() 

                
        
