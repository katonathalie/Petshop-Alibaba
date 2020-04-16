document.getElementById("data").addEventListener('change', function() {
    var data = new Date(this.value);
    if(isDate_(this.value) && data.getFullYear() > 1900)
        document.getElementById("idade").value = calculateAge(this.value);
  });

  function calculateAge(dobString) {
    var dob = new Date(dobString);
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    var birthdayThisYear = new Date(currentYear, dob.getMonth(), dob.getDate());
    var age = currentYear - dob.getFullYear();
    if(birthdayThisYear > currentDate) {
      age--;
    }
    return age;
  }

  function calcular(data) {
    var data = document.form.nascimento.value;
    alert(data);
    var partes = data.split("/");
    var junta = partes[2]+"-"+partes[1]+"-"+partes[0];
    document.form.idade.value = (calculateAge(junta));
  }

  var isDate_ = function(input) {
          var status = false;
          if (!input || input.length <= 0) {
            status = false;
          } else {
            var result = new Date(input);
            if (result == 'Invalid Date') {
              status = false;
            } else {
              status = true;
            }
          }
          return status;
  }