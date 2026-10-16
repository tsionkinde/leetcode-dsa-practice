class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        new=[]
        for i in range(len(number)):
            if number[i] in digit:
                new.append(number[:i]+number[i+1:])

        the_max=new[0]
        for j in range(len(new)):
            if new[j]>the_max:
                the_max=new[j]
        return the_max        

                    



        