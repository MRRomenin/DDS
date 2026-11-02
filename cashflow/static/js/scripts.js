const decimal_input = document.querySelector('#amount');
const send_button = document.querySelector('#button_send');
decimal_input.addEventListener('input', (e) => {
      let val = e.target.value;
      val = val.replace(/^[,.]/, '');
      e.target.value = val.replace(/[^0-9,.]/g, '');
  if (input.validity.valid) {
    button_send.disabled = false;
    input.classList.remove('error');
  } else {
    button_send.disabled = true;
    input.classList.add('error');
  }

})