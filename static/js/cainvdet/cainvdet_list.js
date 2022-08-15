/* 
created by edgard.ramos (ismytv@gmail.com)
generated by alice.bash.v.2203a
jue 11 ago 2022 23:23:49 -05
*/

let g_aDataTable = []
let g_oForm = Object;
let g_oDatagrid = Object;
let g_oModalDialog = Object;
let g_oModalCainvdetu = Object;
let controller_name = '/cainvdet_controller/'

// GLOBALES PERSONALIZADAS
// ----------------------- 
let g_msg = {
    'delete' : 'Desea eliminar producto con id='
}

class FormApp extends Form {
    static FORM = {
        fields : {
            filter_input : 'filter_input',
            filter_clear : 'filter_clear',
            filter_search : 'filter_search',
            // fields personalizados
        }
    }

    constructor(aModal) {
        super(aModal);
    }
    
    set_events_form() {
        document.querySelector(`#${FormApp.FORM.fields.filter_input}`).addEventListener(g_events.event_onkeyup, (e) => {
            console.log(e.key)
            this.controller(Lib.actions.action_events_form, e.target.id, e.type, e.key)
        });
        document.querySelector(`#${FormApp.FORM.fields.filter_clear}`).addEventListener(g_events.event_onclick, (e) => {
            this.controller(Lib.actions.action_events_form, e.target.id, e.type)
        });
        document.querySelector(`#${FormApp.FORM.fields.filter_search}`).addEventListener(g_events.event_onclick, (e) => {
            this.controller(Lib.actions.action_events_form, e.target.id, e.type)
        });
    }

    init_data() {
        
        let data = {
            action: 'action_refresh',
            show_grid_header: true,
            ca_inv_cab_id: ca_inv_cab_id.value  // input hidden
        }
        
        
        let oController = new Controller(`${controller_name}`, data, action_refresh);
        oController.fetch_action();
        
        setInterval(function() {
            
            let oController = new Controller(`${controller_name}`, data, action_refresh);
            oController.fetch_action();
        }, 10000)
        
        this.init_modal_dialog();
        this.init_modal_cainvdetu();
    }

    init_modal_dialog() {
        let aOption = [
            { option:'cancel', text:'Cancelar', classname:''},
            { option:'ok', text:'Continuar', classname:''}
        ]
        g_oModalDialog = new ModalDialog('modal_dialog', aOption, '');
    }
    init_modal_cainvdetu() {
        let aOption = [
            { option:'cancel', text:'Cancelar', classname:''},
            { option:'ok', text:'Continuar', classname:''}
        ]
        g_oModalCainvdetu = new ModalDialog('modal_cainvdetu', aOption, '');
    }

    action_events_form(element_id, event_id, event_key) {
        switch (element_id) {
            case FormApp.FORM.fields.filter_search:
                event_key = g_key.enter;

            case FormApp.FORM.fields.filter_input:
                if ( event_key == g_key.enter ) {
                    let str_filter = document.querySelector(`#${FormApp.FORM.fields.filter_input}`).value;
                    let aFilter = this.get_filter(str_filter);
                    g_oDatagrid.current_page = g_oDatagrid.current_page_ini = 1;
                    g_oDatagrid.refresh(aFilter, DataGrid.mode_refresh.filter)
                }
                break;
            
            case FormApp.FORM.fields.filter_clear:
                document.querySelector(`#${FormApp.FORM.fields.filter_input}`).value = '';
                g_oDatagrid.refresh(g_aDataTable, DataGrid.mode_refresh.filter);
                document.querySelector(`#${FormApp.FORM.fields.filter_input}`).focus();
                break;

            // logica eventos fields personalizados
        }
    }

    action_modal_open(parms) {
        let modal_id = parms[0];
        let itemm_id
        switch (modal_id) {
            case 'modal_dialog':
                item_id = parms[1];
                g_oModalDialog.item_id = item_id;
                break;
            case 'modal_cainvdetu':
                item_id = parms[1];
                g_oModalCainvdetu.item_id = item_id;
                break;
        }
    }

    action_modal_close(modal_id) {
        console.log('Close modal', modal_id);
    }

    action_datagrid_action(datagrid_id, action_id, item_id) {
        console.log('ACTION_DATAGRID_ACTION', datagrid_id, action_id, item_id);
        switch (datagrid_id) {
            case 'datagrid':
                switch (action_id) {
                    case 'delete':
                        g_oModalDialog.text = `${g_msg['delete']} ${item_id}?`;
                        g_oModalDialog.set_text();
                        //this.controller(Lib.actions.action_modal_open, 'modal_dialog', item_id);
                        this.controller(Lib.actions.action_modal_open, 'modal_cainvdetu', item_id);
                        break;
                    
                    case 'edit':
                        let element = g_aDataTable.find(e => e.id === item_id) 
                        if ( element == undefined) {
                            alert(`No se encontró item ${item_id}`)
                            break;
                        }
                        let data = {
                            action: 'action_list_cainvdetu',
                            cainvdet_id: item_id,
                        }
                        //let oController = new Controller(controller_name, data, action_edit);
                        //oController.fetch_action();
                        let oController = new Controller(controller_name, data, action_list_cainvdetu);
                        oController.fetch_action();
                        break;
                }
                break;
        }
    }

    action_modal_dialog(modal_dialog_id, option) {
        switch (modal_dialog_id) {
            case 'modal_cainvdetu':
                console.log('action modal cainvdetu')
                switch (option) {
                    case 'cancel':
                        this.controller(Lib.actions.action_modal_close, 'modal_cainvdetu');
                        break;
                }
                break;

            case 'modal_dialog':
                switch (option) {
                    case 'ok':
                        console.log('delete', g_oModalDialog.item_id);
                        let data = {
                            action: 'action_delete',
                            id: g_oModalDialog.item_id
                        }
                        let oController = new Controller(controller_name, data, action_delete);
                        oController.fetch_action();
                        this.controller(Lib.actions.action_modal_close, 'modal_dialog');
                        break;

                    case 'cancel':
                        this.controller(Lib.actions.action_modal_close, 'modal_dialog');
                        //this.controller(Lib.actions.action_modal_close, 'modal_cainvdetu');
                        break;
                }
                break;
        }
    }


    /**
     * @function
     * Devuevle una lista filtrada de g_aDataTable
     * @param {*} filter {str}
     * @returns {*} {list of dict}
     */
    get_filter(filter) {
        return g_aDataTable.filter((table) => 
                table.desc.toLowerCase().indexOf(filter.toLowerCase()) != -1);
    }

}

main();

function main() {
    g_oForm = new FormApp(
        [
            {id:'modal_dialog', btn_cancel_id:''},
            {id:'modal_cainvdetu', btn_cancel_id:''}
        ])
    g_oForm.init();
    set_focus(`${FormApp.FORM.fields.filter_input}`);
}

function action_refresh(status, data) {
    if (status !== 200) {
        console.log(`Ocurrió un problema. Status code: ${status}`);
        return;
    }
    init_datagrid(data)
}

function action_edit(status, data) {
    if (status !== 200) {
        console.log(`Ocurrió un problema. Status code: ${status}`);
        return;
    }
    action_redirect(data['action_new']);
}

function action_delete(status, data) {
    if (status !== 200) {
        console.log(`Ocurrió un problema. Status code: ${status}`);
        return;
    }
    if ( data.status !== 200)
        action_redirect('');
    else {
        g_oDatagrid.aData = g_aDataTable = data.aDataTable;
        g_oDatagrid.refresh();
    }
}

function action_list_cainvdetu(status, data) {
    if (status !== 200) {
        console.log(`Ocurrió un problema. Status code: ${status}`);
        return;
    }
    //action_redirect(data['action_new']);
    
    let html = '';
    // Data Producto
    html += `
        <div>Producto: ${data.cainvdet.s_codigo}</div>
        <div>${data.cainvdet.s_descripcion}<div>
        </br>
    `
    // HEADER
    
        let pos_label_size_screen = 0;
       
        let aHeader = [ ['#conteo', 's_ubicacion', 'conteo'] ]
        pos_label_size_screen = (aHeader.length==1)? 0 : is_type_screen(g_min_size_screen.desktop)? 0 : 1;
        //html = ''
        html += '<div class="grid__row grid__row__title">';
        aHeader[pos_label_size_screen].forEach((element, index) => {
            html += _div_grid_column(element, `col_modal_${index+1}`);
        });
        html += '</div>'; // grid__row   
        //document.querySelector(`#modal_cainvdetu`).innerHTML = html;

        // detalles
        for (i=0; i<data.aCaInvDetU.length; i++) {
            let striped = (i % 2 == 0) ? '' : 'grid__row__striped';
            html += `<div class="grid__row ${striped}">`;
            
            html += `<div class="grid__col col_modal_1">`;
            html += `<div class="grid__data ">${data.aCaInvDetU[i].id_conteo}</div>`; 
            html += '</div>'; 
            
            html += `<div class="grid__col col_modal_2">`;
            html += `<div class="grid__data ">${data.aCaInvDetU[i].s_ubicacion}</div>`; 
            html += '</div>'; 

            html += `<div class="grid__col col_modal_3">`;
            html += `<div class="grid__data ">${data.aCaInvDetU[i].ns_conteo}</div>`; 
            html += '</div>'; 
            
            html += `</div>`
        }

        //
        modal_cainvdetu_text.innerHTML = html

    
    //

    //data.aCaInvDetU.forEach(item => {
        //console.log(item.s_ubicacion)


    //});
    
    //modal_cainvdetu_text.innerHTML = 'EDGARDUS'

    modal_cainvdetu.style.display = 'block';
    document.getElementById("modal_cainvdetu").style.display = "block";
    

}

function _div_grid_column(data, class_div_grid__col, class_div_grid__data='') {
    let html = '';
    console.log(class_div_grid__col)
    html += `<div class="grid__col ${class_div_grid__col}">`;
    html += `<div class="grid__data ${class_div_grid__data}">${data}</div>`; 
    html += '</div>'; 
    return html;
}




function _datagrid_action(datagrid_id, action, item_id) {
    console.log('datagrid_action', datagrid_id, action, item_id);
    g_oForm.controller(Lib.actions.action_datagrid_action, datagrid_id, action, item_id);
}

function _action_modal_dialog(modal_dialog_id, option) {
    console.log('action_modal_dialog');
    g_oForm.controller(Lib.actions.action_modal_dialog, modal_dialog_id, option);
}


// FUNCIONALIDAD PERSONALIZADA
// ---------------------------
function init_datagrid(data) {
    g_aDataTable = data.aDataTable;
    g_stock_minimo = data.global_stock_minimo;
    g_oDatagrid = new DataGrid('datagrid',
        g_aDataTable,
        data.aHeader,
        get_data_columns
    );
    g_oDatagrid.refresh();
}

function get_data_columns(item) {
    return [
        { data: item.s_codigo, class: '' },
        { data: item.s_descripcion, class: '' },
        { data: item.unidad_medida_desc, class: '' },
        { data: item.n_stk_act, class: '' },
        { data: item.ns_conteo1, class: (item.count_cainvdetu>0)? 'success':'' },
        { data: item.ns_conteo2, class: '' },
    ]
}


