
class NodeBin():

    def __init__(self, value, sortmethode=lambda a,b: a>=b):
        self.leftNode = None
        self.rightNode = None
        self.value = value
        self.f = sortmethode

    def insert(self, value):
        if self.f(value, self.value): # right
            if self.rightNode == None:
                self.rightNode = NodeBin(value,  self.f)
            else:
                self.rightNode.insert(value)
        
        else:
            if self.leftNode == None:
                self.leftNode = NodeBin(value,  self.f)
            else:
                self.leftNode.insert(value)

    def contain(self, data):
        if data == self.value:
            return True
        else:
            if self.f(data, self.value):
                if self.rightNode == None:
                    return False
                else:
                    return self.rightNode.contain(data)
            
            else:
                if self.leftNode == None:
                    return False
                else:
                    return self.leftNode.contain(data)

    def getInOder(self, array=[]):
        if self.leftNode != None:
            self.leftNode.getInOder(array)
        array.append(self.value)
        if self.rightNode != None:
            self.rightNode.getInOder(array)
        return array

    def getPreOder(self, array=[]):
        array.append(self.value)
        if self.leftNode != None:
            self.leftNode.getInOder(array)
        if self.rightNode != None:
            self.rightNode.getInOder(array)
        return array

    def getInPost(self, array=[]):
        if self.leftNode != None:
            self.leftNode.getInOder(array)
        if self.rightNode != None:
            self.rightNode.getInOder(array)
        array.append(self.value)
        return array

    def isUnival(self):
        if self.leftNode != None and self.leftNode.value != self.value:
            return False
        if self.rightNode != None and self.rightNode.value != self.value:
            return False
        else:
            if self.rightNode != None:
                if not self.rightNode.isUnival():
                    return False
            if self.leftNode != None:
                if not self.leftNode.isUnival():
                    return False
            return True

    def countUnival(self, count=[0]):
        if self.isUnival():
            count[0] += 1
            return count
        
        else:
            if self.leftNode != None:
                self.leftNode.countUnival(count)
            if self.rightNode != None:
                self.rightNode.countUnival(count)
            return count