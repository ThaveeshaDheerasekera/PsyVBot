import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '../configs/url_location.dart';

class UserInputs extends ChangeNotifier {
  // Define the userInputs list
  final List<String> _userInputs = [];

  // Method to get the userInputs list
  List<String> get getUserInputs => _userInputs;

  // Method to add user inputs to the list
  void addUserInput(String input) {
    _userInputs.add(input);
    notifyListeners();
  }

  // Method to clear the userInputs list
  void clearUserInputs() {
    _userInputs.clear();
    notifyListeners();
  }

  Future<dynamic> sendUserInputs(List<String> userInputs) async {
    final url = Uri.parse('${UrlLocation.serverUrl}/sendUserInputs');
    final headers = {
      'Content-Type': 'application/json',
    };
    final body = json.encode(
      {'userInputs': userInputs},
    );

    final response = await http.post(url, headers: headers, body: body);
    // final responseBody = json.decode(response.body);

    if (response.statusCode == 200) {
      return response;
    } else {
      throw Exception('Failed to get prediction: ${response.reasonPhrase}');
    }
  }

  Future<String> getPrediction() async {
    final response =
        await http.get(Uri.parse('${UrlLocation.serverUrl}/getPrediction'));
    if (response.statusCode == 200) {
      final prediction = jsonDecode(response.body)['prediction'];
      return prediction;
    } else {
      throw Exception('Failed to get the prediction');
    }
  }
}
