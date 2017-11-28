from Policy import Policy
class AutoPolicy(Policy):
    def __init__(self,desc,num,premium,VehNum):
        Policy.__init__(self,desc,num,premium):
            self._vNum=VehNum
    def setVehicleIdenificationNumber(self,num):
        self._vNum=num
    def getVehicleIdentificationNumber(self):
        return self._vNum
    def __str__(self):
        display=Policy.__str(self)
        display+="Vehicle Number"
        display+=str(self._vNum)
        return display
if __name__=='__main__':
    autopoly=AutoPolicy()
    autopoly.setPolicyDescription("Car")
    autopoly.setPolicyNum(0001100)
    autopoly.setPolicyPremium(1000.00)
    autopoly.setVehicleIdenificationNumber(147589321)
    autopoly.getPolicyDescription
    autopoly.getPolicyNum
    autopoly.getPolicyPremium
    autopoly.getgetVehicleIdentificationNumber
    print autopoly
    backupauto=AutoPolicy(autopoly.getPolicyDescription,autopoly.getPolicyNum,autopoly.getPolicyPremium,autopoly.getgetVehicleIdentificationNumber)
