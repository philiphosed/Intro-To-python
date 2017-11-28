class Policy:
    """This class tracts the information about one insurance policy"""
    def __init__(self,desc,num,premium):
       """ initialize the data members of the class """
       self._policyDescription = desc
       self._policyNum = num   
       self._policyPremium = premium
    def getPolicyDescription(self):
       """ returns the policy description """
       return self._policyDescription
    def getPolicyNumber(self):
       """ returns the policy number"""
       return self._policyNum
    def getPremium(self):
       """ returns the policy premium amount """
       return self._policyPremium
    def setPolicyDescription(self,d):
       """ assigns the formal parameter to the policy's description """
       self._policyDescription = d
    def setPolicyNum(self,n):
       """ assigns the formal parameter to the policy's number"""
       self._policyNum = n
    def setPolicyPremium(self,amt):
       """ assigns the formal parameter to the policy's monthly premium """
       self._policyPremium = amt
    def __str__(self):
       """ returns a string containing a display of the policy information"""
       printLine = "Policy Descripton " + self._policyDescription
       printLine += "\nPolicy number" + self._policyNum
       printLine += "\nPolicy monthly premium" + str(self._policyPremium)
       return printLine
