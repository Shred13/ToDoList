package com.example.shreyanshanand.todolist

import android.support.v7.widget.RecyclerView
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.fragment_main.*

class RecyclerAdapter (private val names:ArrayList<Names>) : RecyclerView.Adapter<RecyclerAdapter.RowHolder>()  {
//this is a constructor

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerAdapter.RowHolder {
        val inflatedView = parent.inflate(R.layout.fragment_main, false)
        return RowHolder(inflatedView)

    }

    override fun getItemCount(): Int {
        return names.size
    }

    override fun onBindViewHolder(holder: RecyclerAdapter.RowHolder, position: Int) {
        p0.TimeLeft.text = "f"
    }

    class RowHolder(v: View): RecyclerView.ViewHolder(v), View.OnClickListener{
        private var view: View = v

        //3
        init {
            v.setOnClickListener(this)
        }

        //4
        override fun onClick(v: View) {
            Log.d("RecyclerView", "CLICK!")
        }

        companion object {
            //5

        }
    }

}
