var NUM_OF_VERTEXES_DEFAULT = 5;
var numOfVertexes = NUM_OF_VERTEXES_DEFAULT;

window.onload = function(){

    var vertexesNumInput = document.getElementsByName("num_of_vertexes_box");


    vertexesNumInput[0].onfocus = function() {
        //delete info about YOU ENTERED NOT A NUMBER from previos func
        this.placeholder = "";
    };


    vertexesNumInput[0].onblur = function() {
        if (isNaN(this.value)) {
            //if input is not a number
        }
    };


    var enterNum = document.getElementsByName("enter_num");

    enterNum[0].onclick = function() {
        //now we should take number from vertexesNumInput to server or ajax or another func to make table with empty cells
        //= vertexesNumInput[0].placeholder;
        /*var newInput = document.createElement('input');this code makes new input field after clicking on btn with id enter_num
        newInput.type = "text";
        newInput.size = 1;

        document.getElementById("p_before_table").appendChild(newInput);*/
    }
};
