const categorySelect = document.getElementById('categorySelect');
    const subcategorySelect = document.getElementById('subcategorySelect');

    categorySelect.addEventListener('change', function () {
      if (this.value) {
        subcategorySelect.disabled = false;
      } else {
        subcategorySelect.disabled = true;
        subcategorySelect.selectedIndex = 0;
      }
    });