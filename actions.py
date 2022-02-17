# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
import smtplib


class ActionReceiveUserInterest(Action):

    def name(self) -> Text:
        return "action_receive_user_interest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_number")

        return [SlotSet("looking_for", tracker.latest_message['text'])]

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_number")

        return [SlotSet("name", tracker.latest_message['text'])]

class ActionReceivePhoneNumber(Action):

    def name(self) -> Text:
        return "action_receive_phone_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_ex_student")

        return [SlotSet("phone_no", tracker.latest_message['text'])]

class ActionReceiveCompanyName(Action):

    def name(self) -> Text:
        return "action_receive_company_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_number")

        return [SlotSet("company_name", tracker.latest_message['text'])]

class ActionReceiveEmailId(Action):

    def name(self) -> Text:
        return "action_receive_email_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_ex_student")

        return [SlotSet("email_id", tracker.latest_message['text'])]

class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        return [Restarted()]


# Creating new class to send emails.
class ActionEmail(Action):

    def name(self) -> Text:
        # Name of the action
        return "action_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Getting the data stored in the
        # slots and storing them in variables.
        user_name = tracker.get_slot("name")
        user_phone_no = tracker.get_slot("phone_no")
        user_email_id = tracker.get_slot("email_id")
        user_looking_for = tracker.get_slot("looking_for")
        user_company_name = tracker.get_slot("company_name")

        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Making connection secured
        s.starttls()

        # Authentication
        s.login("", "")

        newline = '\n'

        # Message to be sent
        message = f" This is the details of the new user.{newline}\n Name: {user_name}, {newline}\n Contact no: {user_phone_no}, {newline}\n Email Id: {user_email_id}, {newline}\n Interested in: {user_looking_for}, , {newline}\n Company Name: {user_company_name}"

        # Sending the mail
        s.sendmail(from_addr="", to_addrs="", msg=message)

        # Closing the connection
        s.quit()

        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []

class ActionEmailForEmployee(Action):

    def name(self) -> Text:
        # Name of the action
        return "action_email_for_employee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Getting the data stored in the
        # slots and storing them in variables.
        user_digits_code = tracker.get_slot("digits_code")
        user_current_company = tracker.get_slot("current_company")
        user_mobile_number = tracker.get_slot("mobile_number")
        user_email_add = tracker.get_slot("email_add")

        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Making connection secured
        s.starttls()

        # Authentication
        s.login("", "")

        newline = '\n'

        # Message to be sent
        message = f" This is the details of the new user.{newline}\n Name: {user_digits_code} {newline}\n Contact no: {user_current_company} {newline}\n Email Id: {user_mobile_number} {newline}\n Interested in: {user_email_add}"

        # Sending the mail
        s.sendmail(from_addr="", to_addrs="", msg=message)

        # Closing the connection
        s.quit()

        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []