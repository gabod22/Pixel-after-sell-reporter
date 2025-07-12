from .korApi import KordataApi
from .kordataConfig import START_DATE, K_ENDPOING


def get_sales_invoices(progress_callback, on_error, show_dialog):
    progress_callback.emit("Obteniendo facturas de ventas...")
    query_report_list_invoices = {
        "operationName": "some",
        "variables": {},
        "query": 'query some {\n  BasesReportesGenerarReportePorId(\n    data: {id: 100000105}\n    parametros: {columnasAdicionales: [{id: -1, baseCampoId: 2471, seLect: false, wheRe: true, groUp: false, baseReporteCondicionCatalogoId: 25, groupAscendente: null, andOr: "AND", visible: true, esId: false, isDeleted: false, secuencia: -1, baseReporteId: 100000105}], condicionesAdicionales: [{valorInicial: "'
        + START_DATE
        + '", valorFinal: "", baseReporteColumnaId: -1}]}\n  ) {\n    datosListasSeleccion\n    resultadoReporteHashmap\n    baseReporte {\n      id\n      carpetaId\n      parasiteParent\n      compartida\n      esQuery\n      nombreReporte\n      tablaPrincipalId\n      moduloPrincipalId\n      baseReporteTipoId\n      baseReporteIdDetalle\n      basesReportesColumnas {\n        id\n        basesCampos {\n          nombreEtiqueta\n        }\n      }\n      basesReportesPivotConfiguracion {\n        baseReporteColumnaId\n        baseCampoAlias\n        pivotColumna\n        pivotRenglon\n        pivotValor\n      }\n    }\n  }\n}',
    }
    try:
        response = KordataApi(K_ENDPOING).post(query_report_list_invoices)

        invoices = response["data"]["BasesReportesGenerarReportePorId"][
            "resultadoReporteHashmap"
        ][0]["encabezado"]
        invoices.pop(0)
        items = response["data"]["BasesReportesGenerarReportePorId"][
            "resultadoReporteHashmap"
        ][0]["detalle"]
        items.pop(0)
        progress_callback.emit("Facturas de ventas obtenidas correctamente")
        # print(invoices)
        return invoices, items
    except Exception as e:
        print("Error al obtener las facturas de ventas:", e)
        on_error.emit("Error al obtener las facturas de ventas: " + str(e))
        return [], []

    # print(type(data))
    


# @mide_tiempo
def get_sales_notes(progress_callback, on_error, show_dialog):
    progress_callback.emit("Obteniendo facturas de ventas...")
    try:

        query_report_list_sales_notes = {
            "operationName": "some",
            "variables": {},
            "query": 'query some {\n  BasesReportesGenerarReportePorId(\n    data: {id: 100000104}\n    parametros: {columnasAdicionales: [{id: -1, baseCampoId: 2519, seLect: false, wheRe: true, groUp: false, baseReporteCondicionCatalogoId: 25, groupAscendente: null, andOr: "AND", visible: true, esId: false, isDeleted: false, secuencia: -1, baseReporteId: 100000104}], condicionesAdicionales: [{valorInicial: "'
            + START_DATE
            + '", valorFinal: "", baseReporteColumnaId: -1}]}\n  ) {\n    datosListasSeleccion\n    resultadoReporteHashmap\n    baseReporte {\n      id\n      carpetaId\n      parasiteParent\n      compartida\n      esQuery\n      nombreReporte\n      tablaPrincipalId\n      moduloPrincipalId\n      baseReporteTipoId\n      baseReporteIdDetalle\n      basesReportesColumnas {\n        id\n        basesCampos {\n          nombreEtiqueta\n        }\n      }\n      basesReportesPivotConfiguracion {\n        baseReporteColumnaId\n        baseCampoAlias\n        pivotColumna\n        pivotRenglon\n        pivotValor\n      }\n    }\n  }\n}',
        }
        response = KordataApi(K_ENDPOING).post(query_report_list_sales_notes)
        sales_notes = response["data"]["BasesReportesGenerarReportePorId"][
            "resultadoReporteHashmap"
        ][0]["encabezado"]
        sales_notes.pop(0)
        items = response["data"]["BasesReportesGenerarReportePorId"][
            "resultadoReporteHashmap"
        ][0]["detalle"]
        items.pop(0)
        progress_callback.emit("Notas de venta obtenidas correctamente")
        
        return sales_notes, items
    except Exception as e:
        on_error.emit("Error al obtener las notas de venta: " + str(e))
        return [], []
