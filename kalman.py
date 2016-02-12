import numpy as np

class Kalman():
    """ The famous Kalman filter in a simple and  intuitive application"""
    def __init__(self, F = np.array(1), B=np.array(0), H=np.array(1),
P=np.array(1), Q=np.array(0), R=np.array(0.5)):
        self.x=np.array(0)	#Estado estimado
        self.F = F	#Modelo de transicao dos estados
        self.B = B	#Modelo das entradas de controle
        self.H = H	#Modelo de Observacao
        self.P = P	#Matriz de Covariancia
        self.Q = Q	#Covariancia do Processo
        self.R = R	#Covariancia da medida
        self.states = [] #List to keep the history of states

    def update(self,U):
        #Apply the Kalman Estimation phase getting the control variables
        self.x = np.dot(self.F,self.x) + self.B.dot(U)  #Update x^
        self.P = np.dot((np.dot(self.F,self.P)),self.F.transpose()) +\
			self.Q  #Update P
    def correction(self,z):
        #Apply the Kalman correction phase getting the measured variables
        self.K = np.dot(self.P,self.H.transpose())/ \
		(np.dot(self.H,np.dot(self.P,self.H.transpose()))+self.R)
        self.x = self.x + np.dot(self.K,(z-np.dot(self.H,self.x)))
        self.P = np.dot((1-np.dot(self.K,self.H)),self.P)
        self.states.append(self.x)
    def Step(self,Control_Vector,Measuement_Vector):
        # Estimate the state of the system getting the controls applyed
        # and the noisy measuements
        self.update(Control_Vector)
        self.correction(Measuement_Vector)
        return self.x
    def GetState(self):
        return self.x
