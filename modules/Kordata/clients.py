from .korApi import KordataApi
from .kordataConfig import K_ENDPOING
import logging
def get_clients(progress_callback, on_error, show_dialog):
    try:
        progress_callback.emit("Obteniendo clientes...")
        query_report_list_sales_notes = {
            "variables": {},
            "query": '{\n  BasesReportesGenerarConTerminosBusqueda(\n    reporteId: 894\n    terminosBusqueda: [{baseReporteColumnaId: 8564, terminoBusqueda: null, operador: null, ordenamiento: "DESC"}]\n    paginadoInformacion: {numeroPagina: 1, registrosPorPagina: 100000}\n  ) {\n    datosListasSeleccion\n    paginadoCount\n    resultadoReporteHashmap\n    baseReporte {\n      id\n      basesReportesColumnas {\n        id\n        seLect\n      }\n    }\n  }\n}',
        }
        response = KordataApi(K_ENDPOING).post(query_report_list_sales_notes)

        clients = response["data"]["BasesReportesGenerarConTerminosBusqueda"][
            "resultadoReporteHashmap"
        ]
        clients.pop(0)
        progress_callback.emit("Clientes obtenidos correctamente")
        return clients
    except Exception as e:
        logging.error(f"Error al obtener los clientes: {e}", exc_info=True)
        on_error.emit(f"Error al obtener los clientes: {e}")
        return []
        
