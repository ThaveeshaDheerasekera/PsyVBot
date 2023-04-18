import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:google_fonts/google_fonts.dart';
import 'providers/user_inputs.dart';
import 'screens/home_screen.dart';
import 'screens/spash_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => UserInputs()),
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'PsyVBot',
        theme: ThemeData(
          fontFamily: GoogleFonts.oxygenMono().fontFamily,
          primarySwatch: const MaterialColor(
            0xFFC8A2C8,
            {
              50: Color(0xFFF6E9F7),
              100: Color(0xFFEED2EF),
              200: Color(0xFFE5B9E7),
              300: Color(0xFFDC9FDF),
              400: Color(0xFFD586D7),
              500: Color(0xFFCC6DCF),
              600: Color(0xFFC464C7),
              700: Color(0xFFBD4BBF),
              800: Color(0xFFB532B7),
              900: Color(0xFFAD19AF),
            },
          ),
        ),
        home: FutureBuilder(
          future: Future.delayed(Duration(seconds: 5)), // Wait for 3 seconds
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.done) {
              return HomeScreen(); // Navigate to home screen
            } else {
              return SplashScreen(); // Show splash screen
            }
          },
        ),
      ),
    );
  }
}
