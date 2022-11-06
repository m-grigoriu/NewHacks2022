package com.example.homescreen;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;

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
        String kiloString = intent.getStringExtra(Intent.EXTRA_LOCAL_ONLY);
        double kilom = Double.parseDouble(kiloString);

        try {
            Process p = Runtime.getRuntime().exec("cmd /c python " +  "C:\\Users\\zeele\\AndroidStudioProjects\\Stuff\\master.py" + " " + String.valueOf(kilom));
            OutputStream stream = p.getOutputStream(); // <- weird?

            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(stream));

            writer.write(String.valueOf(kilom));
            writer.flush();
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

        ImageView imageView = findViewById(R.id.imageMap);
        imageView.setImageResource(R.drawable.images);
    }
}