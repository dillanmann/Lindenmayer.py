import LSystem

class TurtleLSystem(LSystem):

    def __init__(self):
        self._branching = False
        self._angle = 0
        self._increment = 0
        self._branch_blocks = []

    def Generate(self, x, y):

        self._nodes += Block(x, y)

        for rule in self._rules:
            for character in rule:
                self.Interpret(character, self._angle, self._increment)

        for block in self._branch_blocks:
            self._nodes += block
        self._branch_blocks.clear()


    def Interpret(self, next, angle, increment):
        if self._branching:
            if (next != '[' and next != ']'):
                self._branch.top().AppendRule(next)
        else:
            # Standard non-branching interpretation
            if next == self._axiom:
                # Move forward in heading 1 unit
                deltas = GetDelta(angle)
                self._nodes += Block(self._nodes[self.GetSize - 1]->getPosition().x + (self._nodes[self.GetSize - 1] ->self.GetSize.x * deltas.x), self._nodes[
                        self.GetSize - 1]->getPosition().y + (self._nodes[self.GetSize - 1]->self.GetSize.y * deltas.y))));
            elif next == '+':
                angle += increment;

            elif next == '-':
                angle -= increment

        # start new branch
        if next == '[':
            if not self._branch:
                # if empty, use current non-branch as start
                self.AddBranch(self._nodes.back()->getPosition(), self._increment)
                self._branching = True
            else:
                # otherwise create a start point from top of stack
                # then push new nodes
                self._branch.top()->AddBranch(self._branch.top()->self._nodes.back()->getPosition(), self._increment)

        elif next == ']':

            # If branch is not empty, get nodes then pop
            if self._branch:
                # Generate nodes from top system
                newPos = self._nodes.back()->getPosition();
                self._branch.top()->Generate(newPos.x, newPos.y);

                # Get nodes from top branch
                nodes = self._branch.top()->GetData();
                self._branch.pop();

                for i in range(0, len(nodes)):
                    self._branch_blocks += nodes[i]

                # if branch is empty after popping, stop branching
                if not self._branch:
                    self._branching = False;

    def GetDelta(self, angle):

        # Uses equation of circle(Cos / Sin) to get position  of next block
        x = cos(DJM::ConvertRads(angle))
        y = sin(DJM::ConvertRads(angle))

        if IsClose(x, 0.0):
            x = 0.0
        if IsClose(y, 0.0):
            y = 0.0

        return Vector2f(x, y)

    def GenerateRandom(self, size, posMin, posMax, increment):

        rules = ""

        # More F's than other symbols to weight it toward more Fs and angle changes.'
        # TODO; weighted random
        axiom = "FFFF+-[]"
        axiomSize = len(axiom)

        self._axiom = 'F';
        self._angle = 0;
        self._increment = increment;

        #std::cout << "Generating system of length: " << size << " and increment: " << increment << std::endl;

        if self._nodes:
            self._nodes.clear()
            self._nodes.resize(0)

        # Generate rule string from random elements of axiom string
        for i in range(0, size)
            rules += axiom[GetRandom(0, axiomSize)]

        # Find difference between boundaries then use to generate random starting point
        # within the boundaries
        diff = Vector2f(posMax.x - posMin.x, posMax.y - posMin.y)

        # Push initial node at random starting position
        self._nodes += Block(GetRandom(0, diff.x + posMin.x), GetRandom(0, diff.y - posMin.y))

        # Interpret rules, char by char
        for i in range(0, size):
            Interpret(rules[i], self._angle, self._increment)

        for block in self._branch_blocks:
            self._nodes += block

    def AddBranch(self, pos, increment):
        # Push new branch onto stack
        self._branch += TurtleLSystem()

        # Initialize branch attributes
        self._branch.top()->Initialize(self._axiom, "", self._angle, self._increment)
        self._branch.top()->AddBlock(pos)