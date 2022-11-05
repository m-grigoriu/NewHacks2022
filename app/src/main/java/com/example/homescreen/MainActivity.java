package com.example.homescreen;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    String type = "miles";
    double distance = 0;
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
        spinnerUnits.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                type = parent.getItemAtPosition(position).toString();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                type = "each";
            }
        });

    }

    public void distanceRoute(View view) {
        EditText distanceEdit = findViewById(R.id.editDistance);
        distance = Integer.valueOf(String.valueOf(distanceEdit.getText()));
        Intent intent = new Intent(this, MapsActivity.class);
        if (type.equals("kilometers")){
            distance = distance / 1.609;
        }
        intent.putExtra(Intent.EXTRA_LOCAL_ONLY, String.valueOf(distance));
        startActivityForResult(intent, 5);
    }

    public void caloriesRoute(View view) {
        EditText distanceEdit = findViewById(R.id.editCalories);
        distance = Integer.valueOf(String.valueOf(distanceEdit.getText()));
        Intent intent = new Intent(this, MapsActivity.class);
        intent.putExtra(Intent.EXTRA_LOCAL_ONLY, String.valueOf(distance/100));
        startActivityForResult(intent, 5);
    }

}