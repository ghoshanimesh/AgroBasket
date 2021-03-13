import 'package:AgroBasket/cropStatus/cropStatus.dart';
import 'package:AgroBasket/dashboard/dashboardHome.dart';
import 'package:AgroBasket/login/login.dart';
import 'package:AgroBasket/util/colors.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';

class DashBoard extends StatefulWidget {
  @override
  _DashBoardState createState() => _DashBoardState();
}

class _DashBoardState extends State<DashBoard> {
  int _currentIndex = 0;
  final List<Widget> _children = [
    DashBoardHome(),
    CropStatus(),
  ];

  void onTabTapped(int index) {
    setState(() {
      _currentIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          toolbarHeight: 70,
          centerTitle: true,
          backgroundColor: white,
          automaticallyImplyLeading: false,
          elevation: 0,
          title: RichText(
            text: TextSpan(
              children: <TextSpan>[
                TextSpan(
                    text: 'agro',
                    style: GoogleFonts.nunitoSans(
                        textStyle: TextStyle(
                            color: primary_green,
                            fontSize: 32,
                            fontWeight: FontWeight.bold))),
                TextSpan(
                  text: 'basket',
                  style: GoogleFonts.nunitoSans(
                    textStyle: TextStyle(
                        color: primary_basket,
                        fontSize: 32,
                        fontWeight: FontWeight.bold),
                  ),
                ),
              ],
            ),
          ),
          actions: [
            IconButton(
              icon: Icon(Icons.logout),
              padding: EdgeInsets.all(5),
              onPressed: () async {
                SharedPreferences prefs = await SharedPreferences.getInstance();
                await prefs.clear();
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => Login()),
                );
              },
              color: secondary_green,
            )
          ],
        ),
        bottomNavigationBar: BottomNavigationBar(
          selectedItemColor: primary_green,
          unselectedItemColor: black,
          currentIndex: _currentIndex,
          onTap: onTabTapped,
          items: [
            BottomNavigationBarItem(
              icon: new Icon(Icons.home),
              label: 'Home',
            ),
            BottomNavigationBarItem(
              icon: new Icon(Icons.track_changes),
              label: 'Crop Status',
            ),
          ],
        ),
        body: _children[_currentIndex]);
  }
}
