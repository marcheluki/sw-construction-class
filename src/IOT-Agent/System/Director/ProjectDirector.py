
#Generic director
from Generic.Director.GenericProjectDirector import GenericProjectDirector

#Local imports
from System.App.VideoProcedures.VideoProcedures import VideoProcedures

#Director class
class ProjectDirector( GenericProjectDirector ):

    #-----------------------------------------------------------------------------------------------------------------------------
    def __init__( self, ):
        """
        Class builder, all the contextual configurations are charged from the base class (borg pattern) in a shared state
        Returns:
            [None]: None
        """
        super().__init__(
                {
                    '__project': {
                        '__name': 'iot-agent',
                        '__label': 'iot-agent',
                    },
                }
            )
    
    #-----------------------------------------------------------------------------------------------------------------------------
    def __play( self, what, value_a, value_b ):
        """
        Main API starter objects flux
        """
        #Initial procedure log
        self.ctx['__obj']['__log'].setLog( 'Iniciando ...' )
        self.ctx['__obj']['__log'].setDebug( self.ctx )        
        #Step 01: Calling HDP reader procedure
        VideoProcedures().readRTSPStreaming()
        #Bye
        return None
    
    #-----------------------------------------------------------------------------------------------------------------------------
    def setFlux( self, argv ):
        """
        Main API starter objects multiprocessing
        """
        #Main argument
        try:
            what = argv[1]
        except:
            what = None
        #Complementary argument A
        try:
            value_a = argv[2]
        except:
            value_a = None
        #Complementary argument B
        try:
            value_b = argv[3]
        except:
            value_b = None
        #Regular conciliation procedure?
        if (
            what is None or
            what == '-d' 
        ):
            """
                * Examples that you can run on console/shell:
                    a) [ python main.py -d yyyy-mm-dd yyyy-mm-dd ]
                    b) [ python main.py -d yyyy-mm-dd ]
                    c) [ python main.py ] --> This will be TODAY date
            """
            #Playing main conciliation
            self.__play(
                (
                    '-d' if what is None else what 
                ), 
                value_a, 
                value_b 
            )
        #Invalid argument?
        else:
            #Invalid execution argument log
            self.ctx['__obj']['__log'].setLog( 'Argumento de execucion [' + str( what ) + '] invalido' )
        #Goodbye
        return None
    
    #-----------------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def go( argv ):
        """
        Main API starting flux
        """
        ProjectDirector().setFlux( argv )
