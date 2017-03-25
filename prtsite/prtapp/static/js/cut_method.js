var NUM_OF_VERTEXES_DEFAULT = 5;
var numOfVertexes = NUM_OF_VERTEXES_DEFAULT;

window.onload = function(){

   doNewInputs(numOfVertexes);
   //alert("azaza");
   var vertexesNumInput = document.getElementsByName("num_of_vertexes_box");



    vertexesNumInput[0].onfocus = function() {
        //delete info about YOU ENTERED NOT A NUMBER from previos func
        this.placeholder = "";
    };


    vertexesNumInput[0].onblur = function() {
        if (isNaN(this.value)) {
            //if input is not a number
        }
        else {
            document.getElementsByName("enter_num")[0].onclick = function() {
            deletePrevInputs(numOfVertexes);
            doNewInputs(vertexesNumInput[0].value);
            changeWidthToOptimal(vertexesNumInput[0].value);
            };
            numOfVertexes = vertexesNumInput[0].value;
        }
    };



    //function declaration
    function doNewInputs(num) {
           // var vertexesNum = vertexesNumInput[0].value;
        
        for (var i = 0;i < num;i++) {
            for (var j =0 ;j < num;j++) {
            var newInput = document.createElement('input');//this code makes new input field after clicking on btn with id enter_num
            newInput.type = "text";
            newInput.size = 1;
            newInput.className = "added_by_js";
            //newInput.style.float="left";
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
};
