package com.example.homescreen;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.IOException;
import java.io.*;

public class route extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ActionBar actionBar = getSupportActionBar();
        actionBar.hide();

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_route);

        Intent intent = getIntent();
        String mileString = intent.getStringExtra(Intent.EXTRA_LOCAL_ONLY);
        double mile = Double.parseDouble(mileString);

        try {
            Process p = Runtime.getRuntime().exec("python yourapp.py");
            OutputStream stdin = p.getOutputStream(); // <- Eh?

            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(stdin));

            writer.write(String.valueOf(mile));
            writer.flush();
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

        ImageView imageView = findViewById(R.id.imageMap);
        imageView.setImageResource(R.drawable.images);
    }
}