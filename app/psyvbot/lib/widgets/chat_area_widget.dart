import 'package:flutter/material.dart';

class ChatAreaWidget extends StatelessWidget {
  const ChatAreaWidget({
    super.key,
    required this.chatMessages,
    required this.scrollController,
  });

  final List<String> chatMessages;
  final ScrollController scrollController;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: ListView.builder(
        itemCount: chatMessages.length,
        controller: scrollController,
        itemBuilder: (context, index) {
          return Column(
            children: [
              ListTile(
                title: Container(
                  padding: const EdgeInsets.all(10),
                  child: Text(
                    chatMessages[index],
                    style: const TextStyle(fontSize: 14),
                  ),
                ),
              ),
              const Padding(
                padding: EdgeInsets.symmetric(horizontal: 15),
                child: Divider(
                  color: Colors.grey,
                  thickness: 0.5,
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}
