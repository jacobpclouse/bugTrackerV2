// Function used to search tables for characters
function tableSearchFunction() {
    var input, filter, table, tr, td, i, txtValue;

    input = document.getElementById("search-input");
    filter = input.value.toUpperCase();
    table = document.getElementById("issue-table");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
  }


// Below is using js to generate the link for the issue and go there

// function generateLinkForIssue() {
//   var row;
//   // selectedRow

//   // console.log("it works")
//   console.log(document.getElementById("row-id"));
  
// }


// https://stackoverflow.com/questions/29042140/click-on-html-table-and-get-row-number-with-javascript-not-jquery
function  generateLinkForIssue(element) {


  console.log(element)
}