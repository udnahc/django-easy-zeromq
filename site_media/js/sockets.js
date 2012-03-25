function create_note() {
    $.ajax({
       type: "GET",
       url:'/create/',
       success: function(return_value){ 
           $("#popupContact").html(return_value);
           processPopup();;
       },
    });
}

function create_socket() { 
    $.ajax({
        type: "POST",
        url:'/save/',
        data: $("#create_socket_form").serialize(),
        success: function(return_value){
            $("<div class='alert-message success'><a class='close' onClick='close_message();' href='#'>x</a><p>Socket has been created successfully " + return_value + "</p></div>").prependTo("#create_socket") 
            create_socket_in_work_area(return_value)
        }
     });
}

function create_socket_in_work_area(socket_draggable_details){
    var socket_details = $.parseJSON(socket_draggable_details)
    socket_name = socket_details.socket_name
    description = socket_details.description
    port_number = socket_details.port
    python_package = socket_details.python_package
    socket_type = socket_details.socket_type
    $("<div id='" + socket_name + "' style='width:150px; height:150px;'><div>").appendTo("#actual-work-area");
    var socket_html = "<strong>" + socket_name  + "</strong>" + "<h5>" + description + "</h5><h5>" + port_number + "</h5><h5>" + socket_type + "</h5><h5>" + python_package + "</h5>"
    $("#" + socket_name).html(socket_html);
    $("#" + socket_name).resizable()
    $("#" + socket_name).draggable()
    $("#" + socket_name).addClass('ui-widget-content')
}

function close_message() {
    $('.alert-message').remove()
};


function start_everything() {
    $.ajax({
        type: "GET",
        url:'/start_everything/',
     });
};

function stop_everything() {
    $.ajax({
        type: "GET",
        url:'/stop_everything/',
     });
};

function start_processes() {
    $.ajax({
        type: "GET",
        url:'/start_processes/',
    });
};

function stop_processes() {
    $.ajax({
        type: "GET",
        url:'/stop_processes/',
    });
};

function run_project() {
    alert("Run another project will come later boss ");
};