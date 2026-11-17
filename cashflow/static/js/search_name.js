const input_search = document.getElementById("InputSearch");

function searchTransaction()  {
  let input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("InputSearch");
  filter = input.value.toUpperCase();
  table = document.getElementById("table_transaction");
  tr = table.querySelectorAll(".select_item");

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
  const visibleRows = Array.from(tr).filter(tr => tr.offsetParent !== null);
  document.getElementById("text_amount").textContent = `Количество: ${visibleRows.length}`;
}

input_search.addEventListener('input', searchTransaction);
