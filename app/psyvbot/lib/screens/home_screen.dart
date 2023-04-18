import 'package:flutter/material.dart';

import 'chat_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'PsyVBot',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          height: MediaQuery.of(context).size.height,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: const <Widget>[
              Text(
                'Welcome to PsyVBot!',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(height: 20),
              Text(
                'Instructions',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(height: 10),
              Text(
                '1. Start a conversation with PsyVBot by typing a message in the text field and pressing the send button.\n\n2. To clear the conversation and chat history, simply type "clear".\n\n3. To access the instructions while using the chatbot, just type "help".\n\n4. You are not required to greet the chatbot, simply express your concerns or issues.\n\n5. For depression diagnosis, type "diagnose"..\n\n\t --> The output is a number ranging between 0 and 1, where a value closer to 1 (ex: 0.8533554077148438) indicates that you are NOT diagnosed with depression.\n\n\t--> If the number is closer to around 0.5 (ex: 0.4333544077148438), there is a high probability that you may have depression.\n\n\t--> If the number is closer to 0 (ex: 0.2333544077148438), it indicates that you may be diagnosed with depression, which can even lead to suicidal thoughts.\n\n6. To prevent unintentional clearing of the chat, double tap is required to go back to the home page during a conversation.\n\n7. PsyVBot will respond to your messages and offer support as best as it can.\n\n\n*** To obtain an accurate diagnosis, please provide detailed information about your situation.',
                style: TextStyle(
                  fontSize: 16,
                ),
                textAlign: TextAlign.justify,
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          await Navigator.pushAndRemoveUntil(
            context,
            MaterialPageRoute(builder: (context) => const ChatScreen()),
            (Route<dynamic> route) => false,
          );
        },
        child: const Icon(Icons.chat),
      ),
    );
  }
}
