import 'package:flutter/material.dart';

import 'chat_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xFFD586D7),
        title: const Text(
          'PsyVBot',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
      ),
      body: Container(
        height: MediaQuery.of(context).size.height,
        width: MediaQuery.of(context).size.width,
        margin:
            EdgeInsets.only(top: MediaQuery.of(context).size.height * 0.075),
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Welcome to PsyVBot!',
                style: TextStyle(fontSize: 30.0, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 30.0),
              Image.asset(
                'assets/logo/logo.png',
                height: 120,
              ),
              SizedBox(height: 40.0),
              Container(
                padding: EdgeInsets.symmetric(
                    horizontal: MediaQuery.of(context).size.width * 0.1),
                child: Text(
                  'Chatbot platform that aims to help you self-diagnose your mental health condition. By analyzing your input text, our model can predict your level of depression, ranging from happy to suicidal ideation. Our platform utilizes natural language processing techniques and an LSTM model trained on a large corpus of pre-processed Reddit data to provide you with personalized feedback. In addition to text-based communication, our app also features audio output functionality to make it more accessible for users. We believe that by providing users with a tool to self-diagnose their mental health conditions, we can help people seek the necessary support and treatment they need.',
                  style: TextStyle(
                    fontSize: 12,
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
              SizedBox(height: 40.0),
              ElevatedButton(
                onPressed: () async {
                  await Navigator.pushAndRemoveUntil(
                    context,
                    MaterialPageRoute(builder: (context) => const ChatScreen()),
                    (Route<dynamic> route) => false,
                  );
                },
                child: Padding(
                  padding: const EdgeInsets.symmetric(
                      horizontal: 20.0, vertical: 20.0),
                  child: Text(
                    'Start Self-Diagnosis',
                    style: TextStyle(fontSize: 20.0),
                  ),
                ),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Color(0xFFD586D7),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30.0),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}


// Container(
//         color: Color(0xFFF6E9F7),
//         padding: const EdgeInsets.all(20),
//         height: MediaQuery.of(context).size.height,
//         child: SingleChildScrollView(
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             crossAxisAlignment: CrossAxisAlignment.center,
//             children: const <Widget>[
//               Text(
//                 'Welcome to PsyVBot!',
//                 style: TextStyle(
//                   fontSize: 24,
//                   fontWeight: FontWeight.bold,
//                 ),
//               ),
//               SizedBox(height: 20),
//               Text(
//                 'Instructions',
//                 style: TextStyle(
//                   fontSize: 18,
//                   fontWeight: FontWeight.bold,
//                 ),
//               ),
//               SizedBox(height: 10),
//               Text(
//                 '1. Start a conversation with PsyVBot by typing a message in the text field and pressing the send button.\n\n2. To clear the conversation and chat history, simply type "clear".\n\n3. To access the instructions while using the chatbot, just type "help".\n\n4. You are not required to greet the chatbot, simply express your concerns or issues.\n\n5. For depression diagnosis, type "diagnose"..\n\n\t --> The output is a number ranging between 0 and 1, where a value closer to 1 (ex: 0.8533554077148438) indicates that you are NOT diagnosed with depression.\n\n\t--> If the number is closer to around 0.5 (ex: 0.4333544077148438), there is a high probability that you may have depression.\n\n\t--> If the number is closer to 0 (ex: 0.2333544077148438), it indicates that you may be diagnosed with depression, which can even lead to suicidal thoughts.\n\n6. To prevent unintentional clearing of the chat, double tap is required to go back to the home page during a conversation.\n\n7. PsyVBot will respond to your messages and offer support as best as it can.\n\n\n*** To obtain an accurate diagnosis, please provide detailed information about your situation.',
//                 style: TextStyle(
//                   fontSize: 16,
//                 ),
//                 textAlign: TextAlign.justify,
//               ),
//             ],
//           ),
//         ),
//       ),
