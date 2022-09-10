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
function generateLinkForIssueHref(element,uri) {
  // new http request setup
  var xmlHttp = new XMLHttpRequest();

  // selectedRow
  console.log(uri)
  // getting id from inside element
  idForURL = element.children["id-value"].innerText;
  // creating uri
  newURI = uri.concat(idForURL)

  console.log(idForURL);
  console.log(`new uri: ${newURI}`)

  // send request
  xmlHttp.open( "GET", newURI, false ); // FALSE for sync request
  xmlHttp.send ();
  // xmlHttp.send( null );

  // return newURI
  console.log("Request Sent")
}


// function  generateLinkForIssue(element) {

  
//   // Create an XMLHttpRequest object
//   const xhttp = new XMLHttpRequest();
  
//   idForURL = parseInt(element.children[1].innerText);
//   //idForURL = element.children["id-value"].innerText;
//   console.log(idForURL)
//   xhttp.open("POST", "/issue",idForURL);
//   xhttp.send();
  

// -----

// // Below is using js to generate the link for the issue and go there
// function generateLinkForIssueHref(element,uri) {
//   // selectedRow
//   console.log(uri)
//   idForURL = element.children["id-value"].innerText;
//   console.log(idForURL);
//   // "location.href=this.href+'?xyz='+val;return false;"
//   newURI = uri.concat(idForURL)
//   console.log(`new uri: ${newURI}`)
// }
