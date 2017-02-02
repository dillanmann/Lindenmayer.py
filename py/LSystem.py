
class LSystem(object):

    def LSystem(self):
        self._nodes = []

    def Initialize(self, axiom, rules, angle, increment):
        self._axiom = axiom
        self._rules = rules
        self._angle = angle
        self._increment = increment

    def Initialize(self, axiom, rule, angle, increment):
        self._axiom = axiom
        self._rules = [rule]
        self._angle = angle
        self._increment = increment


    def GetSize(self):
        return len(self._nodes)

    def GetElement(self, index):
        return self._nodes[index]

    def GetData(self):
        return self._nodes

    def SetAxiom(self, axiom):
        self._axiom = axiom

    def AddRule(self, rule):
        self._rules += rule

    def SetIncrement(self, increment):
        self._increment = increment

    def AppendRule(self, rule):
        if not self._rules:
            self._rules += ""

        self._rules += rule
