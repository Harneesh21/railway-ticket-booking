document.getElementById("bookingForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const age = document.getElementById("age").value;
  const gender = document.querySelector('input[name="gender"]:checked').value;
  const from = document.getElementById("from").value;
  const to = document.getElementById("to").value;
  const date = document.getElementById("date").value;
  const travelClass = document.querySelector('input[name="class"]:checked').value;
  const tickets = document.getElementById("tickets").value;

  if (from === to) {
    alert("Source and destination cannot be the same.");
    return;
  }

  const confirmationMsg = `
    <strong>Booking Confirmed!</strong><br>
    Passenger: ${name} (${gender}, Age: ${age})<br>
    From: ${from} → To: ${to}<br>
    Travel Date: ${date}<br>
    Class: ${travelClass}<br>
    Tickets: ${tickets}
  `;

  const confirmationDiv = document.getElementById("confirmation");
  confirmationDiv.innerHTML = confirmationMsg;
  confirmationDiv.classList.remove("hidden");

  // Optional: reset form
  document.getElementById("bookingForm").reset();
});
