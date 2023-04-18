import 'package:flutter/material.dart';

import '../screens/home_screen.dart';

class BackButtonWidget extends StatelessWidget {
  const BackButtonWidget({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onDoubleTap: () async {
        FocusScope.of(context).unfocus(); // Unfocus the current focus node
        await Navigator.pushAndRemoveUntil(
          context,
          MaterialPageRoute(builder: (context) => const HomeScreen()),
          (Route<dynamic> route) => false,
        );
      },
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          elevation: 0.0,
        ),
        onPressed: () {},
        child: const Icon(Icons.arrow_back),
      ),
    );
  }
}
