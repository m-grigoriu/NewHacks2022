package com.example.homescreen;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ActionBar actionBar = getSupportActionBar();
        actionBar.hide();

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Spinner spinnerUnits = findViewById(R.id.units);

        final ArrayList<String> units = new ArrayList<>();
        units.add("miles");
        units.add("kilometers");

        ArrayAdapter<String> spinnerArrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, units);
        spinnerArrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinnerUnits.setAdapter(spinnerArrayAdapter);
    }
    public void distanceRoute(View view) {
        Intent intent = new Intent(this, MapsActivity.class);
        //intent.putExtra();
        startActivityForResult(intent, 5);
    }

}