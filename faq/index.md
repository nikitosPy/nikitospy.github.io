  <body class="container mt-5">
    <form onsubmit="sendContact(event)">
      <div class="mb-3">
        <label for="emailInput" class="form-label">Enter your email address</label>
        <input type="email" class="form-control" id="emailInput">
      </div>
      
      <div class="mb-3">
        <label for="messageInput" class="form-label">Enter your message</label>
        <textarea class="form-control" id="messageInput" rows="3"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <script>
      async function sendContact(ev) {
        ev.preventDefault();

        const senderEmail = document
          .getElementById('emailInput').value;
        const senderMessage = document
          .getElementById('messageInput').value;

        const webhookBody = {
          embeds: [{
            title: 'Contact Form Submitted',
            fields: [
              { name: 'Sender', value: senderEmail },
              { name: 'Message', value: senderMessage }
            ]
          }],
        };

        const webhookUrl = 'https://discord.com/api/webhooks/1008733530953613322/GvPmR4Zi5xAWr2who1Ibe6fdlP9rQibI9WFs1Z3ozL-gZwGJX6dQG4nLmd22ftGhYkV7';

        const response = await fetch(webhookUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(webhookBody),
        });

        if (response.ok) {
          alert('I have received your message!');
        } else {
          alert('There was an error! Try again later!');
        }
      }
    </script>
  </body>
</html>
