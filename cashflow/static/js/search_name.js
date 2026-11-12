const input_search = document.getElementById("InputSearch");

function searchTransaction()  {
  let input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("InputSearch");
  filter = input.value.toUpperCase();
  table = document.getElementById("table_transaction");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
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

input_search.addEventListener('input', searchTransaction);
