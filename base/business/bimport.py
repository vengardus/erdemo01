import pandas as pd
from base.libs.excelpd import ExcelPd
import numpy as np
from base.config import ImportSheet

class BImport():
    aSheet = {
        ImportSheet.producto: {
            'sheet_name' : 'PRODUCTOS',
            'aColumn': {
                's_codigo': 0,
                'unidad_medida_s_codigo': 1,
                's_descripcion': 2,
                's_categoria': 3
            },
            'oSheet': None
        },
        ImportSheet.stock: {
            'sheet_name' : 'STOCK',
            'aColumn': {
                's_codigo': 1,
                's_ubicacion': 4,
                'stock': 5,
            },
            'oSheet': None
        },
    }
    aMessage = []
    

    def getExcel(self, filename):
        '''
            Lee los sheet y actualiza el self.aSheet[x]['df'] correspondiente
            
            Parameters:
                filenane : url del excel a leer
            
            Return:
                True si leyo correctamente todos los sheet, False caso contrario
        '''
        ok = False
        oExcelPd = ExcelPd(filename)
        # lee sheet producto
        if not oExcelPd.get_sheet(self.aSheet[ImportSheet.producto]['sheet_name']):
            self.aMessage += oExcelPd.aError_message
        else:
            self.aSheet[ImportSheet.producto]['oSheet'] = oExcelPd.oSheet
            ok = True
        
        # lee sheet stock
        if not oExcelPd.get_sheet(self.aSheet[ImportSheet.stock]['sheet_name']):
            ok = False
            self.aMessage += oExcelPd.aError_message
        else:
            self.aSheet[ImportSheet.stock]['oSheet'] = oExcelPd.oSheet
            
        return ok

    def import_unidad_medida(self):

        ok = False
        print(self.aSheet[ImportSheet.producto]['oSheet'])
        print('name:', self.aSheet[ImportSheet.producto]['oSheet'].df, type(self.aSheet[ImportSheet.producto]['oSheet'].df))
        df_producto:pd.DataFrame = self.aSheet[ImportSheet.producto]['oSheet'].df
        print('producto:', df_producto, type(df_producto))
        
        print('ED1')

        if df_producto.empty:
            self.aMessage.append(f'No hay datos en hoja {self.aSheet[ImportSheet.producto]["sheet_name"]}')
            print('EMPTY')
            return ok
        
        print('ED2')
        print('XXX', self.aSheet[ImportSheet.producto]['aColumn']['unidad_medida_s_codigo'])
        print('YYY')
        df_unidades = pd.DataFrame()
        df_unidades['unidad'] = df_producto.iloc[:,
                        self.aSheet[ImportSheet.producto]['aColumn']['unidad_medida_s_codigo']]
                
        # agrupar df_unidades por columna unidad (una unica fila pñor unidad)
        # groupby devuelve type obj Serie, pero con el reset_ibdex retornaun DF
        # reset_index agrega un indice y mueve las columnas
        df_unidades_group = df_unidades.groupby('unidad').size().reset_index()

        # reemplazar los valores en blanco por nan
        df_unidades_group['unidad'].replace('', np.nan, inplace=True)
                
        # eliminar filas que contengan valores nan
        df_unidades_group = df_unidades_group.dropna()
                
        # rename columnas 
        # la 1era columna paso a ser 'unidad', luego del reset_index)
        # la columna con el count es 0                
        df_unidades_group = df_unidades_group.rename(columns={0:'count'})

        # recorrer df_unidades_group
        for _, row in df_unidades_group.iterrows():
            print('row', row['unidad'], row['count'])

        ok = True

        return ok

    def import_sheets(self):
        self.import_unidad_medida()


