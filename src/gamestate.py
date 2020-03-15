# Simplify tree-like games
#
# Author: Will Allen

class GameStateException(Exception):
    pass

class GameState:
    def __init__(self):
        self.states = {}
        self.stateArgs = {}
        self.stateKwargs = {}
        self.stateTransitions = {}
        self.stateTransitionDefaults = {}
        self.values = {}
        self.defaultValue = None

    def addState(self, name, function, args=(), kwargs={}):
        self.states[name] = function
        self.stateArgs[name] = args
        self.stateKwargs[name] = kwargs

    def removeState(self, name):
        del self.states[name]
        del self.stateArgs[name]
        del self.stateKwargs[name]

    def addTransition(self, fromState, toState, onRetVal=None):
        if onRetVal is None:
            self.setDefaultTransition(fromState, toState)
        else:
            if fromState not in self.stateTransitions:
                self.stateTransitions[fromState] = {}
            self.stateTransitions[fromState][onRetVal] = toState

    def removeTransition(self, fromState, onRetVal):
        if fromState in self.stateTransitions:
            del self.stateTransitions[fromState][onRetVal]

    def setDefaultTransition(self, fromState, toState):
        self.stateTransitionDefaults[fromState] = toState

    def hasTransition(self, fromState, onRetVal):
        return fromState in self.stateTransitions and onRetVal in self.stateTransitions[fromState]

    def hasDefaultTransition(self, fromState):
        return fromState in self.stateTransitionDefaults

    def nextState(self, currentState, retVal):
        if self.hasTransition(currentState, retVal):
            return self.stateTransitions[currentState][retVal]
        elif self.hasDefaultTransition(currentState):
            return self.stateTransitionDefaults[currentState]
        else:
            raise GameStateException("no relevant state or default state found")

    def getValue(self, key):
        if key in self.values:
            return self.values[key]
        else:
            return self.defaultValue

    def setValue(self, key, value):
        self.values[key] = value

    def hasValue(self, key):
        return key in self.values

    def setDefaultValue(self, value):
        self.defaultValue = value

    def callFunction(self, state):
        return self.states[state](*self.stateArgs[state], **self.stateKwargs[state])

    def start(self, startState, endState=None):
        currentState = startState
        while currentState != endState:
            retVal = self.callFunction(currentState)
            currentState = self.nextState(currentState, retVal)
        self.callFunction(currentState)
