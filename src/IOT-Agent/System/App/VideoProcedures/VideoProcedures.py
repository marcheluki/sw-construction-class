import time
import cv2
import matplotlib.pyplot as plt
#Local imports
from Generic.Global.Borg import Borg
#Director class
class VideoProcedures(Borg):

    #Contextual generic objects
    __ctx = None

    #Configuration data
    __config = None

    #-----------------------------------------------------------------------------------------------------------------------------
    def __init__( self, config = None ):
        """
        Class builder, all the contextual configurations are charged from the base class (borg pattern) in a shared state
        Returns:
            [None]: None
        """
        #Setting contextual generic objects
        super().__init__()
        #Setting config globals
        self.__config = config
        self.frames = None
        #Bye
        return None
    
    #-----------------------------------------------------------------------------------------------------------------------------
    def readRTSPStreaming( self ):
        """
        Reads RTSP Streming of the IP cameras. 
        Detonated with console instruction like: 
            a) [ python main.py ]
        Args:
            filters ([list]): Filter data in a list of dicts.
                               
        Returns:
            list: A list of dicts with the collected values
        """
        #Setting initial time mark for reader procedure
        timemark = time.perf_counter()
        #Reader starting log
        self.ctx['__obj']['__log'].setLog( 'Comenzando la captura de las cámaras IP' )
	    #Parsing rtsp urls
        rtsp = self.ctx['__obj']['__config'].get('rtsp')
	    #Capturing frames of the cameras
        self.frames = {k: cv2.VideoCapture(rtsp[k]).read()[1] for k in rtsp.keys() if cv2.VideoCapture(rtsp[k]).read()[0]} 
        plt.imshow(self.frames['main'])
        plt.show()
        #Reader resume log
        self.ctx['__obj']['__log'].setLog(
            'Lectura finalizada con tiempo de [' + str( time.perf_counter() - timemark ) + '] seg.'
        )
        #Retuning a list of dicts
        return [ {} ]
