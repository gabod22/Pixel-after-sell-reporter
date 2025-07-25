TRELLO_DESCRIPTION_TEMPLATE = (
        "## Cliente \n"
        "nombre: {client_name} - {client_phone} \n"
        "usuario: {user_name} - {user_phone} \n"
        "### Modelo \n {model} \n"
        "### Problema \n {issue} \n \n "
        "### Dirección \n [Dirección] \n"
        "### Información de venta\n"
        "Nota/Factura: {not_fac} \n"
        "Fecha de compra: {buy_date}  \n\n"
        "Vendedor: {seller} \n"
        "Días restantes de garantía: {left_days}"
    )

TRELLO_CARD_NAME_TEMPLATE = "{phone} - {name} - {not_fac}"

TRELLO_CARD_NAME_TEMPLATE_OS = "{phone} - {name} - {not_fac} - {service_order}"