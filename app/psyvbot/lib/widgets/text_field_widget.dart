import 'package:flutter/material.dart';

class TextFieldWidget extends StatelessWidget {
  const TextFieldWidget({
    super.key,
    required TextEditingController controller,
  }) : _controller = controller;

  final TextEditingController _controller;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: TextField(
        style: const TextStyle(
          fontSize: 14,
          color: Colors.black,
        ),
        autofocus: true,
        keyboardType: TextInputType.multiline,
        maxLines: 5, // Set fix height
        controller: _controller,
        decoration: InputDecoration(
          hintText: 'Type your message...',
          contentPadding:
              const EdgeInsets.symmetric(horizontal: 15, vertical: 7.5),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(7),
            borderSide: BorderSide(color: Colors.grey.shade300),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(7),
            borderSide: BorderSide(color: Colors.grey.shade300),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(7),
            borderSide: const BorderSide(color: Color(0xFFC8A2C8)),
          ),
        ),
      ),
    );
  }
}
