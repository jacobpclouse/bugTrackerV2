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


function  generateLinkForIssue(element) {

  
  // Create an XMLHttpRequest object
  const xhttp = new XMLHttpRequest();
  
  idForURL = parseInt(element.children[1].innerText);
  //idForURL = element.children["id-value"].innerText;
  console.log(idForURL)
  xhttp.open("POST", "/issue",idForURL);
  xhttp.send();
  


  // ------
  // use this with jquery to get new url
  // https://stackoverflow.com/questions/8981798/make-table-row-clickable
  // https://stackoverflow.com/questions/20355455/how-to-set-flask-url-for-in-jquery
  //return idForURL

  // --
    // -- https://www.youtube.com/watch?v=V9Uwrmgu-oE
    // $().click(function(){
    //   var itemId = { number: `${idForURL}`}
    // })
}



// function elementFunction(element) {

//   idForURL = parseInt(element.children[1].innerText);  // do something to get a user id from the page
//   const SCRIPT_ROOT = {{ request.script_root|tojson }};
//   // console.log(idForURL)
//   let user_url = `${SCRIPT_ROOT}/issue/${user_id}`
//   console.log(user_url)
// };


function getVarFunc(){
  
}