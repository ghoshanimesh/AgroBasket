import 'package:AgroBasket/dashboard/buyProduct.dart';
import 'package:AgroBasket/dashboard/productCard.dart';
import 'package:AgroBasket/services/posts.dart';
import 'package:AgroBasket/util/colors.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class DashBoardHome extends StatefulWidget {
  @override
  _DashBoardHomeState createState() => _DashBoardHomeState();
}

class _DashBoardHomeState extends State<DashBoardHome> {
  Future<Object> _posts;

  @override
  void initState() {
    _posts = Posts().getPosts();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        color: white,
        padding: EdgeInsets.fromLTRB(20, 5, 20, 15),
        child: FutureBuilder(
          future: _posts,
          builder: (context, snapshot) {
            print(snapshot.hasData);
            if (snapshot.hasData) {
              print(snapshot.data.length);
              if (snapshot.data.length > 0) {
                return ListView.builder(
                    itemCount: snapshot.data.length,
                    itemBuilder: (ctxt, index) {
                      dynamic data = snapshot.data[index];
                      print(data);
                      return ProductCard(
                          data['crop'][0]['cropName'],
                          data['company'][0]['companyName'],
                          data['crop'][0]['cropImage'],
                          data['duration'],
                          data['price'], () {
                        showModalBottomSheet(
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.only(
                                  topLeft: Radius.circular(20.0),
                                  topRight: Radius.circular(20.0)),
                            ),
                            context: context,
                            builder: (BuildContext buildContext) {
                              return BuyProduct(data);
                            });
                      });
                    });
              } else {
                print("Here length 0");
                return Center(
                  child: Text(
                    "Company has no requirements.",
                    style: GoogleFonts.nunitoSans(
                      textStyle: TextStyle(
                          fontWeight: FontWeight.w800,
                          fontSize: 16,
                          color: black,
                          height: 0,
                          letterSpacing: 0),
                    ),
                  ),
                );
              }
            } else {
              print("Here");
              return Container();
            }
          },
        ));
  }
}
