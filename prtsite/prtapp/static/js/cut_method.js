var NUM_OF_VERTEXES_DEFAULT = 5, MIN_NUM_OF_VERTEXES = 1, MAX_NUM_OF_VERTEXES = 41;//41 is not obligatorily
var numOfVertexes = NUM_OF_VERTEXES_DEFAULT;

window.onload = function(){

   doNewInputs(numOfVertexes);
   var vertexesNumInput = document.getElementsByName("num_of_vertexes_box");
   var inputError = false;


    vertexesNumInput[0].onfocus = function() {
        this.placeholder = "";
    };


    vertexesNumInput[0].onblur = function() {
        if (isNaN(this.value)) { //if input is not a number
            var err_label = document.getElementById("err_label");
            err_label.innerHTML = "Ошибка. Введите число, пожалуйста.";
            err_label.style.opacity = "1";
            err_label.style.color = "red";
            inputError = true;

        } else  if (this.value < MIN_NUM_OF_VERTEXES || this.value > MAX_NUM_OF_VERTEXES){
            var err_label = document.getElementById("err_label");
            err_label.innerHTML = "Ошибка. Введите число от 1 до 40.";
            err_label.style.opacity = "1";
            err_label.style.color = "red";
            inputError = true;

        } else {
            var err_label = document.getElementById("err_label");
            err_label.style.opacity = "0";
            inputError = false;
        };
    };

    document.getElementsByName("enter_num")[0].onclick = function() {
        if (!inputError) {
            deletePrevInputs(numOfVertexes);
            doNewInputs(vertexesNumInput[0].value);
            changeWidthToOptimal(vertexesNumInput[0].value);
            numOfVertexes = vertexesNumInput[0].value;
        };
    };


    var csrftoken = getCookie('csrftoken');//to pass csrf token defense

    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
    });


    $("#ok_btn").click(function() {
        var inputsValues = [];
        var inpStr ="";
        for (var i = 0; i < numOfVertexes * numOfVertexes; i++) {
            inputsValues.push($(".txt_input").eq(i).val());
            inpStr += inputsValues[i] + ";";
        };

        $.ajax({
            url: "/xhr-test",
            data: { inp: inpStr },
            method: "POST",
            success: function (data) {
                delPrevRes();
                showNewRes(data);
            }
        });
    });


    //function declaration
    function doNewInputs(num) {
        
        for (var i = 0;i < num;i++) {
            for (var j = 0 ;j < num;j++) {

            var newInput = document.createElement('input');//this code makes new input field after clicking on btn with id enter_num
            newInput.type = "text";
            newInput.size = 1;
            newInput.className = "added_by_js txt_input";
            document.getElementById("p_before_table").appendChild(newInput);
            };

            var newBr = document.createElement('br');
            document.getElementById("p_before_table").appendChild(newBr);
            newBr.className = "added_by_js";
        };
    };


    function deletePrevInputs(num) {

        var elemsToDel = document.getElementsByClassName("added_by_js");
        var len = elemsToDel.length;
        for (var i=len-1;i >= 0;i--){//reverse loop. Because in usual loop len decreases and in some moment i becomes more than 
            elemsToDel[i].parentNode.removeChild(elemsToDel[i]);//existed elements in collection. So error:index is out of range.
        };
    };


    function changeWidthToOptimal(num) {
        if (document.getElementById("content").offsetWidth < num * document.getElementsByClassName("added_by_js")[0].offsetWidth) {
            document.getElementById("p_before_table").style.width = 
            (+num + 1) * (document.getElementsByClassName("added_by_js")[0].offsetWidth) + "px";
        };// + 1 - to have some free space right
    };


    function getCookie(name) {//from django docs. It's to pass csrf token defense using AJAX
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        };
      };
    };
    return cookieValue;
    };


    function delPrevRes() {
        prevRes = document.getElementById("result");
        prevRes.parentNode.removeChild(prevRes);
    };

    function showNewRes(data) {
        var newP = document.createElement('p'); //to show result
        newP.id = "result"
        if (typeof(+data) == "number") {
            data = "Корнем является вершина номер " + data + ".";
        }
        var node = document.createTextNode(data);
        newP.appendChild(node);
        document.getElementById("p_before_table").appendChild(newP);
    };
};
