function bookTicket() {
  const from = document.getElementById("from").value;
  const to = document.getElementById("to").value;
  const tickets = document.getElementById("tickets").value;
  const travelClass = document.querySelector('input[name="class"]:checked').value;

  if (from === to) {
    alert("Source and destination cannot be the same.");
    return;
  }

  alert(`Ticket Booked!\nFrom: ${from}\nTo: ${to}\nClass: ${travelClass}\nTickets: ${tickets}`);
}
