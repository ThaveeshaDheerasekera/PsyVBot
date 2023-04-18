import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';

class StopSpeakButtonWidget extends StatelessWidget {
  const StopSpeakButtonWidget({
    super.key,
    required this.flutterTts,
  });

  final FlutterTts flutterTts;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        elevation: 0.0,
      ),
      onPressed: () async {
        await flutterTts.stop();
      },
      child: const Icon(Icons.stop_circle_outlined),
    );
  }
}
