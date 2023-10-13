import requests

def send_notification(incident_id):
  """Sends a notification to the TC using the given incident ID."""

  # Replace this with your preferred method of sending a notification
  # For example, you could use this to send an email to the TC members:
  #
   requests.post("https://api.email-service.com/send-email",
                json={"to": ["ejiro.laureld@gmail.com"], "subject": "New incident opened", "body": "Incident ID: {}".format(incident_id)})

  # Or, you could use this to post a message to a Slack channel:
  #
  # requests.post("https://hooks.slack.com/services/...",
  #              json={"text": "New incident opened: {}".format(incident_id)})

if __name__ == "__main__":
  incident_id = open("incident_id.txt", "r").read()
  send_notification(incident_id)
